from __future__ import annotations

import datetime
from typing import Optional
from typing import Union

import attrs
import pandas
from pyspark.sql import dataframe as pyspark_dataframe
from typeguard import typechecked

from tecton import conf
from tecton._internals import display
from tecton._internals import errors
from tecton._internals import metadata_service
from tecton._internals import sdk_decorators
from tecton.interactive import data_frame as tecton_dataframe
from tecton.interactive import run_api
from tecton.interactive import snowflake_api
from tecton.interactive import spark_api
from tecton.unified import common as unified_common
from tecton.unified import utils as unified_utils
from tecton_core import fco_container
from tecton_core import feature_definition_wrapper
from tecton_core import feature_set_config
from tecton_core import specs
from tecton_proto.args import fco_args_pb2
from tecton_proto.args import feature_view_pb2 as feature_view__args_pb2
from tecton_proto.common import fco_locator_pb2
from tecton_proto.data import feature_view_pb2 as feature_view__data_pb2
from tecton_proto.metadataservice import metadata_service_pb2


@attrs.define
class FeatureView(unified_common.BaseTectonObject):
    """Base class for Feature View classes (including Feature Tables).

    Attributes:
        _feature_definition: A FeatureDefinitionWrapper instance, which contains the Feature View spec for this Feature
            View and dependent FCO specs (e.g. Data Source specs). Set only after the object has been validated. Remote
            objects, i.e. applied objects fetched from the backend, are assumed valid.
        _args: A Tecton "args" proto. Only set if this object was defined locally, i.e. this object was not applied
            and fetched from the Tecton backend.
    """

    _feature_definition: Optional[feature_definition_wrapper.FeatureDefinitionWrapper] = attrs.field(repr=False)
    _args: Optional[feature_view__args_pb2.FeatureViewArgs] = attrs.field(repr=False, on_setattr=attrs.setters.frozen)

    @property
    def _spec(self) -> Optional[specs.FeatureViewSpec]:
        return self._feature_definition.fv_spec if self._feature_definition is not None else None

    def _build_args(self) -> fco_args_pb2.FcoArgs:
        if self._args is None:
            raise errors.BUILD_ARGS_INTERNAL_ERROR

        return fco_args_pb2.FcoArgs(feature_view=self._args)

    @classmethod
    @typechecked
    def _create_from_data_proto(
        cls, proto: feature_view__data_pb2.FeatureView, fco_container: fco_container.FcoContainer
    ) -> "FeatureView":
        """Create a new Feature View object from a data proto."""
        spec = specs.create_feature_view_spec_from_data_proto(proto)
        feature_definition = feature_definition_wrapper.FeatureDefinitionWrapper(spec, fco_container)
        info = unified_common.TectonObjectInfo.from_data_proto(proto.fco_metadata, proto.feature_view_id)
        return cls(info=info, feature_definition=feature_definition, args=None, source_info=None)

    @property
    def _is_valid(self) -> bool:
        return self._spec is not None

    @sdk_decorators.sdk_public_method
    def validate(self) -> None:
        # TODO
        pass

    @sdk_decorators.sdk_public_method
    @unified_utils.requires_remote_object
    def summary(self) -> display.Displayable:
        """Displays a human readable summary of this data source."""
        request = metadata_service_pb2.GetFeatureViewSummaryRequest(
            fco_locator=fco_locator_pb2.FcoLocator(id=self._spec.id_proto, workspace=self._spec.workspace)
        )
        response = metadata_service.instance().GetFeatureViewSummary(request)
        return display.Displayable.from_fco_summary(response.fco_summary)

    def _construct_feature_set_config(self) -> feature_set_config.FeatureSetConfig:
        feature_set_config = feature_set_config.FeatureSetConfig()
        feature_set_config._add(self._feature_definition)
        if self._feature_definition.is_on_demand:
            raise NotImplementedError("ODFVs require adding in depedendent feature view defintions.")
        return feature_set_config


class BatchFeatureView(FeatureView):
    @sdk_decorators.sdk_public_method
    @unified_utils.requires_validation
    def get_historical_features(
        self,
        spine: Optional[
            Union[pyspark_dataframe.DataFrame, pandas.DataFrame, tecton_dataframe.TectonDataFrame, str]
        ] = None,
        timestamp_key: Optional[str] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        entities: Optional[
            Union[pyspark_dataframe.DataFrame, pandas.DataFrame, tecton_dataframe.TectonDataFrame]
        ] = None,
        from_source: bool = False,
        save: bool = False,
        save_as: Optional[str] = None,
    ) -> tecton_dataframe.TectonDataFrame:
        """TODO(jake): Port over docs. Deferring to avoid skew while in development."""

        # TODO(jake): Port over get_historical_features() error checking. Deferring because we'll be reworking
        # from_source defaults. See TEC-10489.

        if conf.get_bool("ALPHA_SNOWFLAKE_COMPUTE_ENABLED"):
            return snowflake_api.get_historical_features(
                spine=spine,
                timestamp_key=timestamp_key,
                start_time=start_time,
                end_time=end_time,
                entities=entities,
                from_source=from_source,
                save=save,
                save_as=save_as,
                feature_set_config=self._construct_feature_set_config(),
                append_prefix=False,
            )

        return spark_api.get_historical_features_for_feature_definition(
            feature_definition=self._feature_definition,
            spine=spine,
            timestamp_key=timestamp_key,
            start_time=start_time,
            end_time=end_time,
            entities=entities,
            from_source=from_source,
            save=save,
            save_as=save_as,
        )

    @sdk_decorators.sdk_public_method
    @unified_utils.requires_validation
    def run(
        self,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        aggregation_level: Optional[str] = None,
        **mock_sources: Union[pandas.DataFrame, pyspark_dataframe.DataFrame],
    ) -> tecton_dataframe.TectonDataFrame:
        """TODO(jake): Port over docs. Deferring to avoid skew while in development."""
        if self._feature_definition.is_temporal and aggregation_level is not None:
            raise errors.FV_UNSUPPORTED_AGGREGATION

        if conf.get_bool("ALPHA_SNOWFLAKE_COMPUTE_ENABLED"):
            return snowflake_api.run_batch(
                fd=self._feature_definition,
                feature_start_time=start_time,
                feature_end_time=end_time,
                mock_inputs=mock_sources,
                aggregate_tiles=None,
                aggregation_level=aggregation_level,
            )

        return run_api.run_batch(
            self._feature_definition,
            start_time,
            end_time,
            mock_sources,
            feature_definition_wrapper.FrameworkVersion.FWV5,
            aggregate_tiles=None,
            aggregation_level=aggregation_level,
        )

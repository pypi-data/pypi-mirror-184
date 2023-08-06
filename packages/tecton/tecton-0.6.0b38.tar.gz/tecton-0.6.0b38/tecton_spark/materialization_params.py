from typing import List

import attrs

from tecton_core.feature_definition_wrapper import FeatureDefinitionWrapper
from tecton_spark.time_utils import convert_timestamp_to_epoch

DIAGNOSTIC_DATE_FORMAT = "%Y-%m-%d %H:%M:%S %Z"


@attrs.define
class MaterializationParams(object):
    """
    Holds the configuration for scheduled materializations.
    """

    _fdw: FeatureDefinitionWrapper

    def construct_anchor_times(self, start_time, num_tiles, version) -> List[int]:
        """Creates `num_tiles` consecutive anchor_times starting from `start_time`.

        :return: An increasing list of consecutive anchor times.
        """
        anchor_times = []
        for i in range(num_tiles):
            anchor_time = start_time + i * self._fdw.get_tile_interval
            anchor_time_val = convert_timestamp_to_epoch(anchor_time, version)
            anchor_times.append(anchor_time_val)

        return anchor_times

    def construct_tile_end_times(self, latest_tile_end_time, num_tiles, version) -> List[int]:
        """Creates `num_tiles` consecutive tile_end_times where latest one ends at `latest_tile_end_time`.

        :return: An increasing list of consecutive tile end times.
        """
        tile_end_times = []
        for i in range(num_tiles):
            tile_end_time = latest_tile_end_time - i * self._fdw.batch_materialization_schedule
            time_val = convert_timestamp_to_epoch(tile_end_time, version)
            tile_end_times.append(time_val)

        tile_end_times.reverse()
        return tile_end_times

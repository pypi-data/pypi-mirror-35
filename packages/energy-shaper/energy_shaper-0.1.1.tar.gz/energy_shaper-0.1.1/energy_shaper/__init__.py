"""
    energy_shaper
    ~~~~~
    Given energy readings, split and group into given energy load shapes/profiles
"""

PROFILE_DEFAULT = [0.05, 0.07, 0.12, 0.11,
                   0.14, 0.14, 0.27, 0.10
                   ]

ALL_MONTHS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ALL_DAYS = [0, 1, 2, 3, 4, 5, 6]

from energy_shaper.models import Reading, DaySummary

from energy_shaper.splitter import split_into_intervals
from energy_shaper.splitter import split_into_daily_intervals
from energy_shaper.splitter import split_into_profiled_intervals

from energy_shaper.demand_periods import in_peak_day, in_peak_time
from energy_shaper.demand_periods import in_peak_period

from energy_shaper.grouper import get_group_end
from energy_shaper.grouper import group_into_profiled_intervals
from energy_shaper.grouper import group_into_daily_summary

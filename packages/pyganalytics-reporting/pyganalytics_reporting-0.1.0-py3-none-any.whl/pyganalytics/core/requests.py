from typing import List, Union

from pyganalytics.utility.enums import *
from pyganalytics.utility import dr
from pyganalytics.utility.dateranges import DateRange


class ReportRequest(dict):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def view_id(self):
        return self['viewId']

    @property
    def date_ranges(self):
        return self['dateRanges']

    @property
    def sampling_level(self):
        return self['samplingLevel']

    @sampling_level.setter
    def sampling_level(self, value: Union[Sampling, str]):
        if isinstance(value, Sampling):
            self['samplingLevel'] = value
        else:
            self['samplingLevel'] = Sampling[value]

    def add_next_page_token(self, value):
        self['pageToken'] = value

    def has_next_page_token(self):
        return True if 'pageToken' in self else False

    def copy(self, date_range: Union[List[DateRange], DateRange, None] = None) -> 'ReportRequest':
        if date_range is None:
            date_range = [dr.last_seven_days]
        if not isinstance(date_range, list):
            date_range = [date_range]
        if len(date_range) > 2:
            raise ValueError('May not assign more than two date ranges in a single report request.')
        return ReportRequest(**self, dateRanges=date_range)







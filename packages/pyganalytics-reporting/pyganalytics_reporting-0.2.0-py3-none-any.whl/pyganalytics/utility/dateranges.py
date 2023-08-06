from dateutil.relativedelta import *
from datetime import date
import isodate
import calendar

from typing import List

from pyganalytics.exceptions import InvalidDateRange, DateBeyondPresent

__all__ = ['dr']


class DateRange(dict):

    def __init__(self, start: str, end: str):
        self._validate_range(isodate.parse_date(start), isodate.parse_date(end))
        super().__init__(startDate=start, endDate=end)

    def __setitem__(self, key: str, value: str):
        if key not in ['startDate', 'endDate']:
            raise KeyError('Only startDate and endDate may be set!')
        else:
            if key == 'startDate':
                self._validate_range(isodate.parse_date(value), isodate.parse_date(self['endDate']))
            elif key == 'endDate':
                self._validate_range(isodate.parse_date(self['startDate']), isodate.parse_date(value))
            super().__setitem__(key, value)

    @staticmethod
    def _validate_range(start, end):
        if start > end:
            raise InvalidDateRange('Start date "{}" cannot be after end date "{}"'.format(start, end))

    @property
    def signature(self):
        return self['startDate'] + '-' + self['endDate']


class DateRangeUtility(object):

    def __init__(self):
        self._current_year = 2018

    @property
    def today(self) -> date:
        return date.today()

    @property
    def last_seven_days(self):
        """The last full seven days (excluding "today"). This is the default used when no date range is specified."""
        yesterday = self.today + relativedelta(days=-1)
        seven_days_ago = self.today + relativedelta(days=-7)
        return DateRange(seven_days_ago.isoformat(), yesterday.isoformat())


    @property
    def last_week(self):
        """The last week from Monday to Sunday."""
        last_sunday = self.today + relativedelta(weekday=SU(-1))
        last_monday = last_sunday + relativedelta(weekday=MO(-1))
        return DateRange(last_monday.isoformat(), last_sunday.isoformat())

    def year(self, year) -> DateRange:
        if year == self.today.year:
            end_date = self.today.isoformat()
        else:
            end_date = '{}-12-31'.format(year)

        start_date = '{}-01-01'.format(year)

        return DateRange(start_date, end_date)

    def yearly(self, start: int, end: int) -> List[DateRange]:
        if end > self.today.year:
            raise DateBeyondPresent('EndDate is beyond current year: {}'.format(end))

        if start > end:
            raise InvalidDateRange('Start date needs to be before the end date.')

        ranges = list()
        for year in range(start, end + 1):
            ranges.append(self.year(year))
        return ranges

    def months(self, year: int):
        if year == self.today.year:
            last_month = DateRange(self.all_months(year)[self.today.month - 1:self.today.month][0]['startDate'],
                                   self.today.isoformat())
            beginning = self.all_months(year)[0:self.today.month - 1]
            beginning.append(last_month)
            return beginning
        else:
            return self.all_months(year)

    def monthly(self, start: int, end: int) -> List[DateRange]:
        if end > self.today.year:
            raise DateBeyondPresent('EndDate is beyond current year: {}'.format(end))

        if start > end:
            raise InvalidDateRange('Start date needs to be before the end date.')

        ranges = list()
        for year in range(start, end + 1):
            ranges.extend(self.months(year))
        return ranges

    def all_months(self, year):
        return [self.january(year), self.february(year), self.march(year), self.april(year), self.may(year),
                self.june(year), self.july(year), self.august(year), self.september(year), self.october(year),
                self.november(year), self.december(year)]

    @staticmethod
    def january(year):
        return DateRange('{}-01-01'.format(year), '{}-01-31'.format(year))

    @staticmethod
    def february(year):
        if calendar.isleap(year):
            return DateRange('{}-02-01'.format(year), '{}-02-29'.format(year))
        else:
            return DateRange('{}-02-01'.format(year), '{}-02-28'.format(year))

    @staticmethod
    def march(year):
        return DateRange('{}-03-01'.format(year), '{}-03-31'.format(year))

    @staticmethod
    def april(year):
        return DateRange('{}-04-01'.format(year), '{}-04-30'.format(year))

    @staticmethod
    def may(year):
        return DateRange('{}-05-01'.format(year), '{}-05-31'.format(year))

    @staticmethod
    def june(year):
        return DateRange('{}-06-01'.format(year), '{}-06-30'.format(year))

    @staticmethod
    def july(year):
        return DateRange('{}-07-01'.format(year), '{}-07-31'.format(year))

    @staticmethod
    def august(year):
        return DateRange('{}-08-01'.format(year), '{}-08-31'.format(year))

    @staticmethod
    def september(year):
        return DateRange('{}-09-01'.format(year), '{}-09-30'.format(year))

    @staticmethod
    def october(year):
        return DateRange('{}-10-01'.format(year), '{}-10-31'.format(year))

    @staticmethod
    def november(year):
        return DateRange('{}-11-01'.format(year), '{}-11-30'.format(year))

    @staticmethod
    def december(year):
        return DateRange('{}-12-01'.format(year), '{}-12-31'.format(year))


dr = DateRangeUtility()

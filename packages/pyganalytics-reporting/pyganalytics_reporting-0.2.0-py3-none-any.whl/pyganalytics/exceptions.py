

class PyGAnalyticsError(Exception):
    pass


class InvalidDateRange(PyGAnalyticsError):
    """The defined date range is invalid."""


class DateBeyondPresent(PyGAnalyticsError):
    """Dates beyond present cannot be used."""


class APIError(PyGAnalyticsError):
    """Base exception for all API error wrappers."""


class ServerError(APIError):
    """A Google Server Error."""

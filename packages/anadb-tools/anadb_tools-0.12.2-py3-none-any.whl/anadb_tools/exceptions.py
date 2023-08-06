"""
Common Exceptions

"""


class AnaDBToolsError(Exception):
    pass


class ConnectionError(AnaDBToolsError):
    pass


class InactiveAnalyticsDatabase(AnaDBToolsError):
    pass


class NoAnalyticsDatabase(AnaDBToolsError):
    pass


class OperationError(AnaDBToolsError):
    pass

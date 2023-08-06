from pyganalytics.utility.enums import MetricType


class Metric(dict):
    """

    :param alias:
    :param expression:
    :param formatting_type:
    """

    def __init__(self, alias: str, expression: str, formattingType: MetricType = MetricType.INTEGER):
        super().__init__(alias=alias, expression=expression, formattingType=formattingType)

    def __setitem__(self, key, value):
        if key not in ['alias', 'expression', 'formattingType']:
            raise KeyError(key)
        else:
            super().__setitem__(key, value)



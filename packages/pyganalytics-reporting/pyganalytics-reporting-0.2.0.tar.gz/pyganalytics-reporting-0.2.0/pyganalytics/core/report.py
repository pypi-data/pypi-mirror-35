from pyganalytics.utility.enums import MetricType

class BaseReport(dict):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def next_page_token(self):
        try:
            return self['nextPageToken']
        except KeyError:
            return None

    def to_key_value_report(self):
        return KeyValueReport(**self)


class OutputReport(object):

    def append(self, base_report: BaseReport):
        raise NotImplemented


class KeyValueReport(OutputReport, dict):

    def __init__(self, base_report: BaseReport):
        super().__init__()

        self._dimension_name: str = base_report['columnHeader']['dimensions'][0]
        self._metric_name: str = base_report['columnHeader']['metricHeader']['metricHeaderEntries'][0]['name']
        self._metric_type = MetricType[base_report['columnHeader']['metricHeader']['metricHeaderEntries'][0]['type']]
        if self._metric_type == MetricType.INTEGER:
            self._value_converter = int
        if 'rows' in base_report['data']:
            self.append(base_report)

    def append(self, base_report: BaseReport):
        for item in base_report['data']['rows']:
            self[item['dimensions'][0]] = self._value_converter(item['metrics'][0]['values'][0])

    @property
    def dimension(self) -> str:
        return self._dimension_name

    @property
    def metric(self) -> str:
        return self._metric_name





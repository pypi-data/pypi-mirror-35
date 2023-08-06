from collections.abc import Iterator
from typing import List

from pyganalytics.core.requests import ReportRequest
from pyganalytics.core.report import BaseReport


class RequestIterator(Iterator):

    def __init__(self, client):
        self._client = client
        self._requests: List[ReportRequest] = list()

    def add_request(self, value: ReportRequest):
        self._requests.append(value)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._requests) == 0:
            raise StopIteration
        response = self._client.reporting.batch_get(self._requests)
        reports = list()
        print(response)
        for report in response['reports']:
            reports.append(BaseReport(**report))

        for i, report in enumerate(reports):
            if report.next_page_token:
                self._requests[i].add_next_page_token(report.next_page_token)
            else:
                self._requests.remove(self._requests[i])

        return reports

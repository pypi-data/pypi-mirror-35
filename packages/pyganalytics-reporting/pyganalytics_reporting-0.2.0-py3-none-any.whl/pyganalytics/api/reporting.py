
import logging
import time

from apiclient import discovery
from googleapiclient.errors import HttpError


class GoogleAnalyticsReportingAPIv4(object):

    def __init__(self, credentials, retries=3, logger=logging.getLogger(__name__), **kwargs):

        self.service = discovery.build(serviceName='analyticsreporting', version='v4', credentials=credentials)
        self.logger = logger
        self.retries = retries
        self.seconds_per_quota = kwargs.get('seconds_per_quota', 100)

    def batch_get(self, report_request, **kwargs):
        """

        :param report_request:
        :param kwargs:
        :return:
        """
        if isinstance(report_request, list):
            body = {'reportRequests': report_request}
        else:
            body = {'reportRequests': [report_request]}
        return self._execute_requests(self.service.reports().batchGet(body=body, **kwargs))

    def _execute_requests(self, request):
        try:
            response = request.execute(num_retries=self.retries)
        except HttpError as error:
            if error.resp['status'] == '429':
                time.sleep(self.seconds_per_quota)
                response = request.execute(num_retries=self.retries)
            else:
                raise
        return response


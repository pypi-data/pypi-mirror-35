import re
import warnings
import os
import logging


from google_auth_httplib2 import AuthorizedHttp

from pyganalytics.api.reporting import GoogleAnalyticsReportingAPIv4


class Client(object):

    def __init__(self, credentials, **kwargs):
        self.logger = logging.getLogger(__name__)
        self.reporting = GoogleAnalyticsReportingAPIv4(credentials,
                                                       retries=kwargs.get('retries', 3),
                                                       logger=kwargs.get('logger', logging.getLogger(__name__)))
"""Module for communicating with the IWWB web service."""

from iwwb.eventlist.interfaces import IIWWBSearcher
from suds.client import Client
from zope.interface import implements

import logging

logger = logging.getLogger('iwwb.eventlist')

WSDL_URL = 'http://www.iwwb.de/wss/sucheIWWBServer.php?wsdl'
RESULTS_PER_PAGE = 50
MAX_RESULTS = 1000


class IWWBSearcher(object):
    """Utility for fetching the results from the IWWWB service"""
    implements(IIWWBSearcher)

    def __init__(self):
        self.client = self._get_service_client()
        self.max_results = RESULTS_PER_PAGE
        self.results_per_page = RESULTS_PER_PAGE

    def _get_service_client(self):
        """Return the service client object for accessing the IWWB service.

        :returns: Service client object
        :rtype: suds.client.Client
        """
        try:
            client = Client(WSDL_URL)
        except:
            # Many things can go wrong
            message = "Can't access the IWWB service."
            logger.exception(message)
            raise Exception(message)
        return client

    def get_results(self, query):
        """Return results from the IWWB service.

        :param query: Dictionary with search parameters and values. For a list
            of possible parameters see:
            http://www.iwwb.de/wss/sucheIWWBServer.php?op=GetFullResult
        :type query: Dictionary
        :returns: List of search results
        :rtype: SearchResult
        """
        try:
            results_array = self.client.service.GetFullResult(
                maxResult=self.max_results,
                resultPerPage=self.results_per_page,
                **query
            )
        except:
            # Many things can go wrong
            message = "Can't parse the IWWB search results."
            logger.exception(message)
            raise Exception(message)

        if results_array.SearchResults:
            results = [res for res in results_array.SearchResults.SearchResult]
        else:
            results = []

        return results

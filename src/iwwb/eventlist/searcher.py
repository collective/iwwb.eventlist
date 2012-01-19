"""Module for communicating with the IWWB web service."""

from iwwb.eventlist.interfaces import IIWWBSearcher
from iwwb.eventlist.config import IWWB_SEARCHER_URL, TAG_PREFIX
from lxml import etree as etree
from urllib2 import urlopen
from zope.interface import implements

import logging

logger = logging.getLogger('iwwb.eventlist')


class IWWBSearcher(object):
    """Utility for fetching the results from the IWWWB service"""
    implements(IIWWBSearcher)

    def get_results(self, keyword):
        url = "%s?suchbegriff_e=%s&angebotsform=0" % (IWWB_SEARCHER_URL, keyword)

        try:
            xml = etree.parse(urlopen(url))
            root = xml.getroot()
            xml_results = root.find(".//%sSearchResults" % TAG_PREFIX).getchildren()
        except:
            # Many things can go wrong
            logger.warning("Can't parse iwwb search results.")
            return []

        results = []

        for result in xml_results:
            event = IWWBEvent()
            event.rank = self._get_attribute(result, 'Rank')
            event.name = self._get_attribute(result, 'Name')
            event.start_time = self._get_attribute(result, 'StartTime')
            event.zip = self._get_attribute(result, 'Zip')
            event.city = self._get_attribute(result, 'City')
            event.type = self._get_attribute(result, 'Type')
            event.title = self._get_attribute(result, 'Type')
            event.keywords = self._get_attribute(result, 'Keywords')
            event.reference_url = self._get_attribute(result, 'ReferenceUrl')
            event.database_supplier = self._get_attribute(
                result, 'DatabaseSupplier'
            )
            event.database_supplier_url = self._get_attribute(
                result, 'DatabaseSupplierURL'
            )
            event.training_supplier = self._get_attribute(
                result, 'TrainingSupplier'
            )
            event.training_supplier_url = self._get_attribute(
                result, 'TrainingSupplierUrl'
            )

            results.append(result)

        return results

    def _get_attribute(self, result, name):
        attr = result.find(".//%s%s" % (TAG_PREFIX, name))

        return attr and attr.text or ''


class IWWBEvent(object):
    """Class that represents an IWWWB Event."""

    def __init__(self):
        self.rank = ''
        self.name = ''
        self.start_time = ''
        self.zip = ''
        self.city = ''
        self.type = ''
        self.title = ''
        self.keywords = ''
        self.reference_url = ''
        self.database_supplier = ''
        self.database_supplier_url = ''
        self.training_supplier = ''
        self.training_supplier_url = ''

# -*- coding: utf-8 -*-
"""Tests for the IWWB Searcher utility."""

from iwwb.eventlist.tests.base import IntegrationTestCase
from iwwb.eventlist.interfaces import IIWWBSearcher
from zope.component import getUtility

import unittest2 as unittest


class TestIWWBSearcher(IntegrationTestCase):
    """Test the IWWBSearcher utility."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.searcher = getUtility(IIWWBSearcher)
        self.searcher.results_per_page = 2

    def test_get_results_empty(self):
        # Search for events in a city that doesn't exist
        query = dict(city='FooBar', page='1')
        self.assertEquals(self.searcher.get_results(query), [])

    def test_get_results_not_empty(self):
        # This search should return some results
        query = dict(city='Berlin', page='1')
        self.assertGreater(len(self.searcher.get_results(query)), 0)

    def test_get_results_format(self):
        query = dict(city='Berlin', page='1')
        results = self.searcher.get_results(query)
        result = results[0]

        # See if we can access the attribute values for a result (we can't test
        # other attributes because they are not mandatory), this should not
        # throw an Attribute error.
        result.Rank
        result.Type

    def test_get_results_false_parameters(self):
        # Try searching with a nonexistent parameter, the method should fail
        query = dict(foo='bar', page='1')
        try:
            self.searcher.get_results(query)
        except:
            pass
        else:
            self.fail("get_results did not raise an Exception!")


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

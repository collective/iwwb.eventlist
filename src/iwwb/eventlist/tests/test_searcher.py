# -*- coding: utf-8 -*-
"""Tests for the IWWB Searcher utility."""

from iwwb.eventlist.tests.base import IntegrationTestCase
from iwwb.eventlist.interfaces import IIWWBSearcher
from zope.component import getUtility

import unittest2 as unittest


class TestSetup(IntegrationTestCase):
    """Test installation of iwwb.eventlist into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']

    def test_searcher_registered(self):
        searcher = getUtility(IIWWBSearcher)
        self.assertIsNotNone(searcher)

    def test_get_results_empty(self):
        searcher = getUtility(IIWWBSearcher)

        # Search for a non-existent keyword
        self.assertEquals(searcher.get_results('238fjjfj99jd'), [])

    def test_get_results(self):
        searcher = getUtility(IIWWBSearcher)

        # Search for a keyword which should return some results
        self.assertGreater(len(searcher.get_results('Rhetorik')), 0)


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

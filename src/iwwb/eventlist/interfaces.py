# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from iwwb.eventlist import _
from plone.theme.interfaces import IDefaultPloneLayer
from zope.interface import Interface
from zope import schema


class IIWWBEventlistLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class IIWWBSearcher(Interface):
    """Interface for the utility for handling communication with the IWWB web
    service.
    """


class IListEventsForm(Interface):
    """Field definition for List Events form."""

    keywords = schema.TextLine(
        title=_(u'Keywords'),
        description=_(u'Enter the search keywords.'),
    )

    all_words = schema.Bool(
        title=_(u'All keywords'),
        description=_(u'Select this if you want to search for all keywords.'),
    )

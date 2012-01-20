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

    query = schema.TextLine(
        title=_(u'Keywords'),
        description=_(u'Enter the search keywords.'),
        required=False,
    )
    allWords = schema.Bool(
        title=_(u'All keywords'),
        description=_(u'Select this if you want to search for all keywords.'),
        required=False,
    )
    city = schema.TextLine(
        title=_(u'City'),
        description=_(u'Enter the city.'),
        required=False,
    )
    startTime = schema.Date(
        title=_(u'Event start'),
        description=_(u'Enter the event start date.'),
        required=False,
    )
    startTimeRequired = schema.Bool(
        title=_(u'Only events with start date'),
        description=_(u'If the event does not have the date information it '
                      'will not be listed.'),
        required=False,
    )
    type = schema.Choice(
        title=_(u'Event type'),
        description=_(u'Select the event type.'),
        vocabulary='iwwb.eventlist.vocabularies.EventTypes',
        required=False,
        default=0,
    )
    sort = schema.Choice(
        title=_(u'Sort by'),
        vocabulary='iwwb.eventlist.vocabularies.SortOptions',
        required=False,
        default='Datum',
    )

IWWB_SEARCHABLE_FIELDS = ('query', 'city', 'startTime', 'type', 'sort',)

# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from datetime import date
from datetime import timedelta
from iwwb.eventlist import _
from iwwb.eventlist import check_year_constraint
from plone.theme.interfaces import IDefaultPloneLayer
from zope import schema
from zope.interface import Interface
from zope.interface import Invalid
from zope.interface import invariant


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
        description=_(u'Enter the search keywords. Examples: Seminar, Excel, ' \
            'Berlin, etc.'),
        required=False,
    )
    startDate = schema.Date(
        title=_(u'Date start'),
        description=_(u'Enter the event start date.'),
        required=False,
        default=date.today(),
        constraint=check_year_constraint,
    )
    city = schema.TextLine(
        title=_(u'City'),
        description=_(u'Enter the city. Examples: Berlin, Bonn, etc.'),
        required=False,
    )
    endDate = schema.Date(
        title=_(u'Date end'),
        description=_(u'Enter the event start date.'),
        required=False,
        default=date.today() + timedelta(7),
        constraint=check_year_constraint,
    )
    zip = schema.TextLine(
        title=_(u'Zip code'),
        description=_(u'Enter the zip code. Examples: 12277, 20999, etc.'),
        required=False,
    )
    type = schema.Choice(
        title=_(u'Event type'),
        description=_(u'Select the event type.'),
        vocabulary='iwwb.eventlist.vocabularies.EventTypes',
        required=True,
        default=0,
    )
    # Doesn't work ATM
    #===========================================================================
    # allWords = schema.Bool(
    #    title=_(u'All keywords'),
    #    description=_(u'Select this if you want to search for all keywords.'),
    #    required=False,
    # )
    #===========================================================================

    # Doesn't work ATM
    #===========================================================================
    # startTimeRequired = schema.Bool(
    #    title=_(u'Only events with start date'),
    #    description=_(u'If the event does not have the date information it '
    #                  'will not be listed.'),
    #    required=False,
    # )
    #===========================================================================

    # Doesn't work ATM
    #===========================================================================
    # sort = schema.Choice(
    #    title=_(u'Sort by'),
    #    vocabulary='iwwb.eventlist.vocabularies.SortOptions',
    #    required=True,
    #    default='startTime',
    # )
    #===========================================================================

    @invariant
    def check_enough_data_provided(obj):
        """Check that the user has provided enough data to perform the query."""
        if not (obj.query or obj.city or obj.zip or obj.startDate or obj.endDate):
            raise Invalid(_("You have to fill out at least one of required " \
                "fields: Keywords, City, Zip code, Event Start, Event End"))

    @invariant
    def check_end_date_bigger_than_start(obj):
        if (obj.startDate and obj.endDate) and (obj.startDate > obj.endDate):
            raise Invalid(_("End date must be smaller than start date"))
        return True

IWWB_SEARCHABLE_FIELDS = ('query', 'city', 'zip', 'startDate', 'endDate', 'type', 'sort',)

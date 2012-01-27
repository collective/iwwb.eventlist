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
        description=_(u'Enter the search keywords.'),
        required=False,
    )
    # Doesn't work ATM
    #===========================================================================
    # allWords = schema.Bool(
    #    title=_(u'All keywords'),
    #    description=_(u'Select this if you want to search for all keywords.'),
    #    required=False,
    # )
    #===========================================================================
    city = schema.TextLine(
        title=_(u'City'),
        description=_(u'Enter the city.'),
        required=False,
    )
    startDate = schema.Date(
        title=_(u'Date start'),
        description=_(u'Enter the earliest event start date.'),
        required=False,
        default=date.today(),
        constraint=check_year_constraint,
    )
    endDate = schema.Date(
        title=_(u'Date end'),
        description=_(u'Enter the latest event start date.'),
        required=False,
        default=date.today() + timedelta(7),
        constraint=check_year_constraint,
    )
    # Doesn't work ATM
    #===========================================================================
    # startTimeRequired = schema.Bool(
    #    title=_(u'Only events with start date'),
    #    description=_(u'If the event does not have the date information it '
    #                  'will not be listed.'),
    #    required=False,
    # )
    #===========================================================================
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
        default='startTime',
    )

    @invariant
    def check_enough_data_provided(obj):
        """Check that the user has provided enough data to perform the query."""
        if not (obj.query or obj.city or obj.startDate):
            raise Invalid(
                    _("You have to fill out at least one additional field \
                    (Keywords, City or Even Start)"))


IWWB_SEARCHABLE_FIELDS = ('query', 'city', 'startDate', 'endDate', 'type', 'sort',)

# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from datetime import date
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
        description=_(u'Enter the search keywords. Examples: Seminar, Excel, '
            'Berlin, etc.'),
        required=False,
    )
    startMonth = schema.Date(
        title=_(u'Course Start'),
        description=_(u'Select the month where the course should start'),
        required=False,
        default=date.today(),
        constraint=check_year_constraint,
    )
    zipcity = schema.TextLine(
        title=_(u'Zip or City'),
        description=_(u'Enter the zip code or city.' ),
        required=False,
    )
    type = schema.Choice(
        title=_(u'Event type'),
        description=_(u'Select the event type.'),
        vocabulary='iwwb.eventlist.vocabularies.EventTypes',
        required=True,
        default=0,
    )
    startTimeRequired = schema.Bool(
        title=_(u'Exclude events without dates'),
        description=_(u'If the event does not have the date information it '
                      'will not be listed.'),
        required=False,
        default=True,
    )

    @invariant
    def check_enough_data_provided(obj):
        """Check that the user has provided enough data to perform the query.
        """
        if not (obj.query or obj.zipcity or obj.startMonth or obj.county):
            raise Invalid(_("You have to fill out at least one of required " \
                "fields: Keywords, Zip code or city, Event Start, County"))


IWWB_SEARCHABLE_FIELDS = (
    'query', 'county', 'zipcity', 'startMonth', 'type', 'sort',)

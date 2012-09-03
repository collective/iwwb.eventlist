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
#    county = schema.Choice(
#        title=_(u'County'),
#        description=_(u"Choose a county"),
#        vocabulary='iwwb.eventlist.vocabularies.Counties',
#        required=True,
#        default='alle'
#    )
    startMonth = schema.Date(
        title=_(u'Course Start'),
        description=_(u'Select the month where the course should start'),
        required=False,
        default=date.today(),
        constraint=check_year_constraint,
    )
#    startDate = schema.Date(
#        title=_(u'Date start'),
#        description=_(u'Enter the event start date.'),
#        required=False,
#        default=date.today(),
#        constraint=check_year_constraint,
#    )
#    city = schema.TextLine(
#        title=_(u'City'),
#        description=_(u'Enter the city. Examples: Berlin, Bonn, etc.'),
#        required=False,
#    )
#    endDate = schema.Date(
#        title=_(u'Date end'),
#        description=_(u'Enter the event start date.'),
#        required=False,
#        default=date.today() + timedelta(7),
#        constraint=check_year_constraint,
#    )
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

    # Doesn't work ATM
    #=========================================================================
    # allWords = schema.Bool(
    #    title=_(u'All keywords'),
    #    description=_(u'Select this if you want to search for all keywords.'),
    #    required=False,
    # )
    #=========================================================================

    # Doesn't work ATM
    #=========================================================================
    # sort = schema.Choice(
    #    title=_(u'Sort by'),
    #    vocabulary='iwwb.eventlist.vocabularies.SortOptions',
    #    required=True,
    #    default='startTime',
    # )
    #=========================================================================

    @invariant
    def check_enough_data_provided(obj):
        """Check that the user has provided enough data to perform the query.
        """
        if not (obj.query or obj.zipcity or obj.startMonth or obj.county):
            raise Invalid(_("You have to fill out at least one of required " \
                "fields: Keywords, Zip code or city, Event Start, County"))

    #@invariant
    #def check_end_date_bigger_than_start(obj):
    #    if (obj.startDate and obj.endDate) and (obj.startDate > obj.endDate):
    #        raise Invalid(_("End date must be smaller than start date"))
    #    return True

IWWB_SEARCHABLE_FIELDS = (
    'query', 'county', 'zipcity', 'startMonth', 'type', 'sort',)

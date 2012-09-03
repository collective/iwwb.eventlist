# -*- coding: utf-8 -*-
"""Definitions of vocabularies."""

from iwwb.eventlist import _
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class CountiesVocabulary(object):
    """ Counties """
    implements(IVocabularyFactory)

    def __call__(self, context):
        """Build a vocabulary of counties.
        """
        items = [
            SimpleTerm('alle', 'alle', _(u'alle')),
            SimpleTerm('baw', 'baw', _(u'Baden-Württemberg')),
            SimpleTerm('bay', 'bay', _(u'Bayern')),
            SimpleTerm('bln', 'bln', _(u'Berlin')),
            SimpleTerm('bra', 'bra', _(u'Brandenburg')),
            SimpleTerm('bre', 'bre', _(u'Bremen')),
            SimpleTerm('hh', 'hh', _(u'Hamburg')),
            SimpleTerm('hes', 'hes', _(u'Hessen')),
            SimpleTerm('mvp', 'mvp', _(u'Mecklenburg-Vorpommern')),
            SimpleTerm('nds', 'nds', _(u'Niedersachsen')),
            SimpleTerm('nrw', 'nrw', _(u'Nordrhein-Westfalen')),
            SimpleTerm('rpf', 'rpf', _(u'Rheinland-Pfalz')),
            SimpleTerm('saa', 'saa', _(u'Saarland')),
            SimpleTerm('sac', 'sac', _(u'Sachsen')),
            SimpleTerm('san', 'san', _(u'Sachsen-Anhalt')),
            SimpleTerm('slh', 'slh', _(u'Schleswig-Holstein')),
            SimpleTerm('thu', 'thu', _(u'Thüringen')),
        ]

        return SimpleVocabulary(items)

CountiesVocabularyFactory = CountiesVocabulary()


class EventTypesVocabulary(object):
    """Vocabulary factory for event types."""
    implements(IVocabularyFactory)

    def __call__(self, context):
        """Build a vocabulary of event types.
        """
        items = [
            SimpleTerm(0, 0, _(u'All Events')),
            SimpleTerm(1, 1, _(u'Seminar')),
            SimpleTerm(2, 2, _(u'Distance Learning')),
            SimpleTerm(3, 3, _(u'CBT/WBT/E-Learning')),
        ]

        return SimpleVocabulary(items)

EventTypesVocabularyFactory = EventTypesVocabulary()


class SortOptionsVocabulary(object):
    """Vocabulary factory for sort options."""
    implements(IVocabularyFactory)

    def __call__(self, context):
        """Build a vocabulary of sort options.
        """
        items = [
            SimpleTerm(
                'Treffergenauigkeit',
                'Treffergenauigkeit',
                _(u'Treffergenauigkeit')
            ),
            SimpleTerm('city', 'city', _(u'Ort')),
            SimpleTerm('zip', 'zip', _(u'PLZ')),
            SimpleTerm('startTime', 'startTime', _(u'Datum')),
        ]

        return SimpleVocabulary(items)

SortOptionsVocabularyFactory = SortOptionsVocabulary()

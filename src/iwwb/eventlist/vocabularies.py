# -*- coding: utf-8 -*-
"""Definitions of vocabularies."""

from iwwb.eventlist import _
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class EventTypesVocabulary(object):
    """Vocabulary factory for event types."""
    implements(IVocabularyFactory)

    def __call__(self, context):
        """Build a vocabulary of event types.
        """
        items = [
            SimpleTerm(0, 0, _(u'Alle Angebote')),
            SimpleTerm(1, 1, _(u'Seminare')),
            SimpleTerm(2, 2, _(u'Fernunterricht')),
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
            SimpleTerm('Ort', 'Ort', _(u'Ort')),
            SimpleTerm('PLZ', 'PLZ', _(u'PLZ')),
            SimpleTerm('Datum', 'Datum', _(u'Datum')),
        ]

        return SimpleVocabulary(items)

SortOptionsVocabularyFactory = SortOptionsVocabulary()

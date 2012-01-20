# -*- coding: utf-8 -*-
"""The List Events view."""

from iwwb.eventlist import _
from iwwb.eventlist.interfaces import IListEventsForm
from iwwb.eventlist.interfaces import IIWWBSearcher
from iwwb.eventlist.interfaces import IWWB_SEARCHABLE_FIELDS
from plone.z3cform.layout import FormWrapper
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form import button
from z3c.form import field
from z3c.form import form
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

import logging

logger = logging.getLogger('iwwb.eventlist')


class ListEventsForm(form.Form):
    """The List Events search form based on z3c.form."""
    fields = field.Fields(IListEventsForm)
    label = _(u"List Events")

    # don't try to read Plone root for form fields data, this is only mostly
    # usable for edit forms, where you have an actual context
    ignoreContext = True

    @button.buttonAndHandler(_(u"List Events!"))
    def list_events(self, action):
        """Submit button handler."""
        data, errors = self.extractData()

        if errors:
            self.status = self.formErrorsMessage
            return

    @button.buttonAndHandler(_(u"Reset"))
    def reset_form(self, action):
        """Cancel button handler."""
        url = self.context.portal_url() + "/@@eventlist"
        self.request.response.redirect(url)


class ListEventsFormWrapper(FormWrapper):
    """Subclass FormWrapper so that we can use a custom frame template that
    renders only the form, nothing else.
    """
    index = ViewPageTemplateFile("formwrapper.pt")


class ListEventsView(BrowserView):
    """A BrowserView to display the ListEventsForm along with it's results."""
    index = ViewPageTemplateFile('eventlist.pt')

    def __init__(self, context, request):
        """Override BrowserView's __init__ to create the ListEventsForm
        for later use.
        """
        BrowserView.__init__(self, context, request)
        self.form_wrapper = ListEventsFormWrapper(self.context, self.request)
        self.form_wrapper.form_instance = ListEventsForm(
            self.context, self.request
        )

    def __call__(self):
        """Main view method that handles rendering."""
        # Hide the editable border and tabs
        self.request.set('disable_border', True)

        # Prepare display values for the template
        options = {
            'events': self.get_events(),
        }
        return self.index(**options)

    def update(self):
        """This is needed so that KSS validation from plone.app.z3cform works
        as expected.
        """
        self.form_wrapper.form_instance.update()

    def get_events(self):
        """Get the events for the provided parameters using the IIWWBSearcher
        utility.
        """
        querydict = self._construct_query()
        results = []

        try:
            searcher = getUtility(IIWWBSearcher)
            # XXX: Temporarily set to a low number
            searcher.results_per_page = 3
            if querydict:
                querydict['page'] = 1
                results = querydict and searcher.get_results(querydict)
        except:
            messages = IStatusMessage(self.request)
            messages.addStatusMessage(u"There was an error getting the \
                results, please try again later.", type="error")

        return results

    def _construct_query(self):
        """Parse the searchable fields from the form."""
        querydict = {}

        for field in IWWB_SEARCHABLE_FIELDS:
            value = self.request.get('form.widgets.%s' % field)
            if value:
                querydict[field] = value

        return querydict

    def get_event_type(self, type_id):
        """Get event type title for the provided event type id."""
        factory = getUtility(
            IVocabularyFactory,
            'iwwb.eventlist.vocabularies.EventTypes'
        )
        vocabulary = factory(self.context)

        return vocabulary.getTerm(type_id).title

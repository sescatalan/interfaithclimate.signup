from five import grok
from plone.app.layout.viewlets.interfaces import IAboveContent
from Products.CMFCore.utils import getToolByName
from interfaithclimate.signup.content.statement import IStatement

grok.templatedir('templates')

class statement_viewlet(grok.Viewlet):
        grok.context(IStatement)
        grok.require('zope2.View')
        grok.template('statement_viewlet')
        grok.viewletmanager(IAboveContent)
        
        @property
        def catalog(self):
            return getToolByName(self.context, 'portal_catalog')
        
        def contents(self):
            brains = self.catalog.unrestrictedSearchResults(path={'query':'/'.join(self.context.getPhysicalPath()), 'depth':1}, review_state='published',portal_type='interfaithclimate.signup.signature')
            results = []
            for brain in brains:
                obj = brain._unrestrictedGetObject()
                results.append({'name':str(obj.first_name)+' '+str(obj.last_name),
                                'designation':obj.designation,
                                'organization':obj.organization,
                                'location':str(obj.city)+', '+str(obj.country)})
            return results
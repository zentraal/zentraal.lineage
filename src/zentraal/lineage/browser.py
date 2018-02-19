from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from zope.component import getMultiAdapter
from plone.app.layout.analytics import view


class AnalyticsViewlet(view.AnalyticsViewlet):

    def render(self):
        """render the webstats snippet"""
        ptool = getToolByName(self.context, "portal_properties")
        snippet = safe_unicode(ptool.site_properties.webstats_js)
        lineageutils = getMultiAdapter(
            (sel.context, self.request), name="lineageutils"
        )
        current_childSite = lineageutils.current_childsite
        if current_childSite:
            childSite_snippet = safe_unicode(
                self.context.getField(fname).get(self.context)
            )

        return childSite_snippet or snippet

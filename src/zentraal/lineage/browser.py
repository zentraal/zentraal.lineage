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
            (self.context, self.request), name="lineageutils"
        )
        current_childSite = lineageutils.current_childsite
        if current_childSite:
            local_analytics = current_childSite.getField('analytics').get(
                current_childSite
            )
            if local_analytics:
                snippet = safe_unicode(local_analytics)

        return snippet

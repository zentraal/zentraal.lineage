from archetypes.schemaextender.field import ExtensionField
from zope.component import adapts
from zope.interface import implements
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from Products.Archetypes import atapi

from collective.lineage.interfaces import IChildSite
from zentraal.lineage.interfaces import IZentraalLineageLayer
from zentraal.lineage import _

class ExtenderTextField(ExtensionField, atapi.TextField):
    """ A text field """

class AnalyticsLineageExtender(object):
    adapts(IChildSite)
    implements(IOrderableSchemaExtender, IBrowserLayerAwareExtender)

    layer = IZentraalLineageLayer

    fields = [
        ExtenderTextField('analytics',
            required=False,
            widget = atapi.TextAreaWidget(
                label=_(u"Local Analytics Code"),
                rows=20,
            ),
            default_output_type="text/html",
            allowable_content_types="text/html",
            default_content_type="text/html",
        ),
    ]

    def __init__(self, context):
         self.context = context

    def getFields(self):
        if IChildSite.providedBy(self.context):
            return self.fields
        return []

    def getOrder(self, original):
        """
        'original' is a dictionary where the keys are the names of
        schemata and the values are lists of field names, in order.

        Move leadImage field just after the Description
        """
        default = original.get('default', None)
        return original

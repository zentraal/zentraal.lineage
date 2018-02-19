# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import zentraal.lineage


class ZentraallineageLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=zentraal.lineage)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'zentraal.lineage:default')


ZENTRAAL_lineage_FIXTURE = ZentraallineageLayer()


ZENTRAAL_lineage_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ZENTRAAL_lineage_FIXTURE,),
    name='ZentraallineageLayer:IntegrationTesting'
)


ZENTRAAL_lineage_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ZENTRAAL_lineage_FIXTURE,),
    name='ZentraallineageLayer:FunctionalTesting'
)


ZENTRAAL_lineage_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ZENTRAAL_lineage_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ZentraallineageLayer:AcceptanceTesting'
)

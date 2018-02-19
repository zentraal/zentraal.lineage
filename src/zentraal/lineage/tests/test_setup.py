# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from zentraal.lineage.testing import ZENTRAAL_lineage_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that zentraal.lineage is properly installed."""

    layer = ZENTRAAL_lineage_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if zentraal.lineage is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'zentraal.lineage'))

    def test_browserlayer(self):
        """Test that IZentraalLineageLayer is registered."""
        from zentraal.lineage.interfaces import (
            IZentraalLineageLayer)
        from plone.browserlayer import utils
        self.assertIn(IZentraalLineageLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ZENTRAAL_lineage_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['zentraal.lineage'])

    def test_product_uninstalled(self):
        """Test if zentraal.lineage is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'zentraal.lineage'))

    def test_browserlayer_removed(self):
        """Test that IZentraalLineageLayer is removed."""
        from zentraal.lineage.interfaces import \
            IZentraalLineageLayer
        from plone.browserlayer import utils
        self.assertNotIn(IZentraalLineageLayer, utils.registered_layers())

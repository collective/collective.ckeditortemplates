# -*- coding: utf-8 -*-

from collective.ckeditortemplates import HAS_PLONE_6_AND_MORE
from collective.ckeditortemplates.testing import CKTEMPLATES_FUNCTIONAL_TESTING

import unittest


if HAS_PLONE_6_AND_MORE:
    from Products.CMFPlone.utils import get_installer


class TestSetup(unittest.TestCase):

    layer = CKTEMPLATES_FUNCTIONAL_TESTING

    def setUp(self):
        portal = self.layer["portal"]
        if HAS_PLONE_6_AND_MORE:
            self.installer = get_installer(portal)

    def test_product_installed(self):
        """Test if collective.ckeditortemplates is installed with portal_quickinstaller."""
        if HAS_PLONE_6_AND_MORE:
            self.assertTrue(self.installer.is_product_installed("collective.ckeditortemplates"))

    def test_uninstall(self):
        """Test if collective.ckeditortemplates is cleanly uninstalled."""
        if HAS_PLONE_6_AND_MORE:
            self.installer.uninstall_product("collective.ckeditortemplates")
            self.assertFalse(self.installer.is_product_installed("collective.ckeditortemplates"))

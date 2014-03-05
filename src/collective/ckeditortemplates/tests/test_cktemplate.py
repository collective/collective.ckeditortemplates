# encoding: utf-8
import unittest2

from plone.app.testing import login
from plone.app.testing import logout

from .. import cktemplate
from ..testing import CKTEMPLATES_INTEGRATION_TESTING


class TestCKTemplate(unittest2.TestCase):
    layer = CKTEMPLATES_INTEGRATION_TESTING

    def setUp(self):
        self.restricted_template = cktemplate.CKTemplate(group_restriction=['Reviewers'])
        self.normal_template = cktemplate.CKTemplate(group_restriction=[])
        self.portal = self.layer['portal']

    def tearDown(self):
        logout()

    def test_plone_group_generator(self):
        groups = ['Administrators', 'Reviewers', 'Site Administrators',
                  'AuthenticatedUsers']
        vocabulary = cktemplate.plone_group_generator(self.portal)
        for group in groups:
            try:
                vocabulary.getTerm(group)
            except LookupError:
                self.fail("unknown term: %s" % group)

    def test_can_view(self):
        login(self.portal, 'john')
        self.assertTrue(self.restricted_template.can_view(self.portal))
        self.assertTrue(self.normal_template.can_view(self.portal))
        logout()
        login(self.portal, 'jane')
        self.assertFalse(self.restricted_template.can_view(self.portal))
        self.assertTrue(self.normal_template.can_view(self.portal))
        logout()

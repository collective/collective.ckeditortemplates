# encoding: utf-8
from collective.ckeditortemplates.browser import cktemplatelisting
from collective.ckeditortemplates.testing import CKTEMPLATES_INTEGRATION_TESTING
from mock import Mock
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.textfield import RichTextValue
from Products.CMFPlone.utils import safe_unicode
from zope.publisher.browser import TestRequest

import unittest


class TestCKTemplateListingView(unittest.TestCase):
    layer = CKTEMPLATES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        request = TestRequest()
        self.view = cktemplatelisting.CKTemplateListingView(self.portal,
                                                            request)

    def test_render(self):
        self.view.get_templates = Mock(return_value=[(None, u'/template')])
        self.view.render_template = Mock(return_value=u"{render}")
        render = """CKEDITOR.addTemplates('default',
{
    imagesPath: CKEDITOR.getUrl('../'),
    templates: [
        {render}
    ]
});"""
        self.assertEqual(render, self.view.render())

    def test_render_template(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        template = api.content.create(self.portal.ckeditortemplates, 'cktemplate', 'test1', 'My &quot;title&quot;',
                                      description="Template &quot;description&quot;",
                                      content=RichTextValue(raw=safe_unicode(u'<h1>My title</h1>'),
                                                            mimeType=u"text/html", outputMimeType=u"text/x-html-safe"))
        # the following is not working on python 2
        # template = type('template', (object, ), {
        #     u'title': u'My "title"',
        #     u'custom_icon': True,
        #     u'image': lambda: 'icon.jpg',
        #     u'description': u'Template "description"',
        #     u'html': lambda: u'<h1>My title</h1>'})
        render = (u'{title: "My &quot;title&quot;", '
                  # u'image: "/template/icon.jpg", '
                  u'description: "Template &quot;description&quot;", '
                  u'html: "<h1>My title</h1>"}')
        self.assertEqual(render, self.view.render_template(template, u'/template'))

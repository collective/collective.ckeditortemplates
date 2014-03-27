# encoding: utf-8
import unittest2
from mock import Mock

from zope.publisher.browser import TestRequest

from .. import cktemplatelisting
from ...testing import CKTEMPLATES_INTEGRATION_TESTING


class TestCKTemplateListingView(unittest2.TestCase):
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
        template = type('template', (object, ), {
            u'title': u'My "title"',
            u'custom_icon': True,
            u'image': 'icon.jpg',
            u'description': u'Template "description"',
            u'html': u'<h1>My title</h1>'})
        render = (u'{title: "My &quot;title&quot;", '
                  u'image: "/template/icon.jpg", '
                  u'description: "Template &quot;description&quot;", '
                  u'html: "<h1>My title</h1>"}')
        self.assertEqual(render, self.view.render_template(template, u'/template'))

# encoding: utf-8
from collective.ckeditortemplates import cktemplate
from collective.ckeditortemplates.testing import CKTEMPLATES_INTEGRATION_TESTING

import unittest


class TestCKTemplate(unittest.TestCase):
    layer = CKTEMPLATES_INTEGRATION_TESTING

    def test_html_simple(self):
        template = cktemplate.CKTemplate()
        content = """<h1>My title</h1><p>Lorem ipsum dolor..."""
        template.content = type('content', (object, ), {'raw': content})
        html = """<h1>My title</h1><p>Lorem ipsum dolor...</p>"""
        self.assertEqual(html, template.html())

    def test_html_complex(self):
        template = cktemplate.CKTemplate()
        content = """<p class="a">text1'<a href="b">"text2"</a></p>"""
        template.content = type('content', (object, ), {'raw': content})
        html = """<p class='a'>text1'<a href='b'>&quot;text2&quot;</a></p>"""
        self.assertEqual(html, template.html())

# encoding: utf-8
from five import grok

from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot


class CKTemplateListingView(grok.View):
    grok.context(IPloneSiteRoot)
    grok.name('cktemplate-listing.js')
    grok.require('zope2.View')

    def get_templates(self):
        templates = []
        for brain in self.context.portal_catalog(portal_type='cktemplate',
                                                 review_state=('enabled', )):
            templates.append((brain.getObject(), brain.getPath()))
        return templates

    def render(self):
        self.request.response.setHeader('Content-Type',
                                        'application/javascript')
        template_renders = []
        for template, path in self.get_templates():
            template_renders.append(self.render_template(template, path))
        return """CKEDITOR.addTemplates('default',
{
    imagesPath: CKEDITOR.getUrl('../'),
    templates: [
        %s
    ]
});""" % ", ".join(template_renders)

    def render_template(self, template, path):
        base = ('{title: "%(title)s", %(image)s'
                'description: "%(description)s", '
                'html: "%(html)s"}')
        icon = ''
        if template.custom_icon is not None:
            icon = 'image: "%s/%s", ' % (path, template.image)
        return base % {
            u'title': template.title.replace('"', '&quot;'),
            u'image': icon,
            u'description': template.description.replace('"', '&quot;'),
            u'html': template.html}

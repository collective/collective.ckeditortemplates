# encoding: utf-8

from z3c.form import form


class CKTemplateListingView(form.Form):
    """View used to get a listing of custom ckeditor templates."""

    enabled_states = ('enabled',)

    def get_templates(self):
        """Get enabled templates."""
        templates = []
        for brain in self.context.portal_catalog(portal_type='cktemplate',
                                                 review_state=self.enabled_states):
            templates.append((brain.getObject(), brain.getPath()))
        return templates

    def render(self):
        """Render the javascript view content."""
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
        """Render each template as a javascript dic."""
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

# encoding: utf-8
from bs4 import BeautifulSoup

from zope.i18nmessageid import MessageFactory

from plone.app.contenttypes.content import Folder
from plone.app.contenttypes.content import Document
from plone.app.contenttypes.interfaces import IFolder
from plone.app.contenttypes.interfaces import IDocument
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage
from plone.dexterity.schema import DexteritySchemaPolicy
from plone.supermodel import model
from five import grok

from . import _

PMF = MessageFactory('plone')


class ICKTemplateFolder(model.Schema, IFolder):
    """ Schema for CKEditor template folder """


class CKTemplateFolder(Folder):
    grok.implements(ICKTemplateFolder)


class CKTemplateFolderSchemaPolicy(DexteritySchemaPolicy):
    """ Schema Policy for CKTemplateFolder """

    def bases(self, schema_name, tree):
        return (ICKTemplateFolder, )


class ICKTemplate(model.Schema, IDocument):
    """ Schema for CKEditor template """

    custom_icon = NamedImage(title=_(u'Template Icon'),
                             description=_(u"Icon displayed before the title in the list of templates"),
                             required=False)

    content = RichText(title=_(u'Template content'),
                       description=_(u"The content that will be pasted when the template is used"),
                       required=True)


class CKTemplate(Document):
    grok.implements(ICKTemplate)

    @property
    def image(self):
        return (u"view/++widget++form.widgets.custom_icon/@@download/%s" %
                self.custom_icon.filename)

    @property
    def html(self):
        soup = BeautifulSoup(self.content.raw)
        soup.html.hidden = True
        soup.body.hidden = True

        # Replace quotes in contents
        for element in soup.findAll(text=True):
            text = unicode(element)
            text = text.replace(u'"', u'U+0022')
            text = text.strip()
            element.replaceWith(text)
        # Remove new lines an carriage returns
        content = ''.join(str(soup).splitlines())
        content = content.decode('utf-8')
        content = content.replace('"', "'")
        content = content.replace(u'U+0022', u'&quot;')
        return content.strip()


class CKTemplateSchemaPolicy(DexteritySchemaPolicy):
    """ Schema Policy for CKTemplate """

    def bases(self, schema_name, tree):
        return (ICKTemplate, )

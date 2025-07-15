# encoding: utf-8
from bs4 import BeautifulSoup
from collective.ckeditortemplates import _
from plone.app.contenttypes.content import Document
from plone.app.contenttypes.content import Folder
from plone.app.contenttypes.interfaces import IDocument
from plone.app.contenttypes.interfaces import IFolder
from plone.app.textfield import RichText
from plone.dexterity.schema import DexteritySchemaPolicy
from plone.namedfile.field import NamedImage
from plone.supermodel import model
from Products.CMFPlone.utils import safe_unicode
from zope.i18nmessageid import MessageFactory
from zope.interface import implementer


PMF = MessageFactory("plone")


class ICKTemplateFolder(model.Schema, IFolder):
    """Schema for CKEditor template folder"""


@implementer(ICKTemplateFolder)
class CKTemplateFolder(Folder):

    # This method is used by index methods.
    # If None is returned, the linked content type is not catalogued
    def _getCatalogTool(self):
        return None


class CKTemplateFolderSchemaPolicy(DexteritySchemaPolicy):
    """Schema Policy for CKTemplateFolder"""

    def bases(self, schema_name, tree):
        return (ICKTemplateFolder,)


class ICKTemplate(model.Schema, IDocument):
    """Schema for CKEditor template"""

    custom_icon = NamedImage(
        title=_(u"Template Icon"),
        description=_(u"Icon displayed before the title in the list of templates"),
        required=False,
    )

    content = RichText(
        title=_(u"Template content"),
        description=_(u"The content that will be pasted when the template is used"),
        required=True,
    )


@implementer(ICKTemplate)
class CKTemplate(Document):
    def image(self):
        return (
            u"view/++widget++form.widgets.custom_icon/@@download/%s"
            % self.custom_icon.filename
        )

    def html(self):
        soup = BeautifulSoup(self.content.raw, features="lxml")
        soup.html.hidden = True
        soup.body.hidden = True

        # Replace quotes in contents
        for element in soup.findAll(text=True):
            text = safe_unicode(element)
            text = text.replace(u'"', u"U+0022")
            text = text.strip()
            element.replaceWith(text)
        # Remove new lines and carriage returns
        content = "".join(str(soup).splitlines())
        content = safe_unicode(content)
        content = content.replace('"', "'")
        content = content.replace(u"U+0022", u"&quot;")
        return content.strip()


class CKTemplateSchemaPolicy(DexteritySchemaPolicy):
    """Schema Policy for CKTemplate"""

    def bases(self, schema_name, tree):
        return (ICKTemplate,)

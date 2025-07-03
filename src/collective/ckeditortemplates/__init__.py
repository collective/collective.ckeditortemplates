# encoding: utf-8
from plone import api
from zope.i18nmessageid import MessageFactory


_ = MessageFactory("collective.ckeditortemplates")
PLONE_VERSION = api.env.plone_version()[:3]
HAS_PLONE_6_AND_MORE = int(api.env.plone_version()[0]) >= 6


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

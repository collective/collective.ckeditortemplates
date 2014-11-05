# -*- coding: utf-8 -*-
from plone import api
from Products.CMFCore.utils import getToolByName
from plone.app.dexterity.behaviors.exclfromnav import IExcludeFromNavigation

FOLDER = "ckeditortemplates"


def setupVarious(context):
    site = context.getSite()
    if context.readDataFile('collective.ckeditortemplates_various.txt') is None:
        return

    if not site.get(FOLDER):
        types = getToolByName(site, 'portal_types')
        types.getTypeInfo('cktemplatefolder').global_allow = True
        container = api.content.create(site, "cktemplatefolder", id=FOLDER, title=FOLDER)
        excl = IExcludeFromNavigation(container)
        excl.exclude_from_nav = True
        types.getTypeInfo('cktemplatefolder').global_allow = False
        container.reindexObject()
        catalog = api.portal.get_tool(name='portal_catalog')
        catalog.uncatalog_object(container.absolute_url_path())
    else:
        catalog = api.portal.get_tool(name='portal_catalog')
        portal_types = ['cktemplatefolder']
        for portal_type in portal_types:
            brains = catalog(portal_type=portal_type)
            for brain in brains:
                catalog.uncatalog_object(brain.getObject().absolute_url_path())

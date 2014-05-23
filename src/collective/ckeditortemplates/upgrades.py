# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from plone import api
from plone.app.dexterity.behaviors.exclfromnav import IExcludeFromNavigation

PROFILE = 'profile-collective.ckeditortemplates:default'
FOLDER = "ckeditortemplates"


def install_folder(site):
    folder = site.get(FOLDER)
    if not folder:
        container = api.content.create(site, "Folder", id=FOLDER, title=FOLDER)
        return container
    else:
        return folder


def update_content_folder(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILE)
    site = api.portal.get()
    types = getToolByName(site, 'portal_types')
    types.getTypeInfo('cktemplatefolder').global_allow = True
    container = install_folder(site)
    excl = IExcludeFromNavigation(container)
    excl.exclude_from_nav = True
    types.getTypeInfo('cktemplatefolder').global_allow = False
    container.reindexObject()
    catalog = api.portal.get_tool(name='portal_catalog')
    catalog.uncatalog_object(container.absolute_url_path())


def unindex_alltemplates(context):
    catalog = api.portal.get_tool(name='portal_catalog')
    portal_types = ['cktemplatefolder']
    for portal_type in portal_types:
        brains = catalog(portal_type=portal_type)
        for brain in brains:
            catalog.uncatalog_object(brain.getObject().absolute_url_path())

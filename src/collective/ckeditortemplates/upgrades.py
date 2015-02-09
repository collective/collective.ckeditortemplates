# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from plone import api
from plone.app.dexterity.behaviors.exclfromnav import IExcludeFromNavigation

PROFILE = 'profile-collective.ckeditortemplates:default'
FOLDER = 'ckeditortemplates'


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


def add_dx_language_behavior(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILE)


def remove_dx_language_behavior(context):
    installer = api.portal.get_tool('portal_quickinstaller')
    if installer.isProductInstalled('plone.multilingualbehavior'):
        installer.uninstallProducts(['plone.multilingualbehavior'])

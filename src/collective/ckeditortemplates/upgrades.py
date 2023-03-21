# -*- coding: utf-8 -*-
from collective.ckeditortemplates import PLONE_VERSION
from plone import api
from plone.app.dexterity.behaviors.exclfromnav import IExcludeFromNavigation
from Products.CMFCore.utils import getToolByName


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
    if PLONE_VERSION >= '5.1':
        from Products.CMFPlone.utils import get_installer  # noqa
        installer = get_installer(context)
        if installer.is_product_installed('plone.multilingualbehavior'):
            installer.uninstall_product('plone.multilingualbehavior')
    else:
        installer = api.portal.get_tool('portal_quickinstaller')  # noqa
        if installer.isProductInstalled('plone.multilingualbehavior'):
            installer.uninstallProducts(['plone.multilingualbehavior'])


def update_workflow(context):
    context.runImportStepFromProfile(PROFILE, 'workflow')
    portal_workflow = api.portal.get_tool(name='portal_workflow')
    portal_workflow.updateRoleMappings()

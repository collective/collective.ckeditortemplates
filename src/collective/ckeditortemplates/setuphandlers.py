# -*- coding: utf-8 -*-
from plone import api
from plone.app.dexterity.behaviors.exclfromnav import IExcludeFromNavigation

FODLER="ckeditortemplates"

def setupVarious(context):
    site = context.getSite()
    if context.readDataFile('collective.ckeditortemplates_various.txt') is None:
        return

    if not api.content.get(FODLER):
        container = api.content.create(site, "cktemplatefolder", title=FODLER)
        excl = IExcludeFromNavigation(container)
        excl.exclude_from_nav = True
        container.reindexObject()

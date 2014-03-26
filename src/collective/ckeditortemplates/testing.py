# encoding: utf-8
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE

from plone import api
from plone.testing import z2

from zope.configuration import xmlconfig


class CollectiveCKTemplatesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.ckeditor
        xmlconfig.file(
            'configure.zcml',
            collective.ckeditor,
            context=configurationContext
        )

        import collective.ckeditortemplates
        xmlconfig.file(
            'configure.zcml',
            collective.ckeditortemplates,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.ckeditortemplates:default')

        api.user.create(email='john@doe.com', username='john')
        api.user.create(email='jane@doe.com', username='jane')

        api.group.add_user(groupname='Reviewers', username='john')
        api.group.add_user(groupname='Administrators', username='jane')


CKTEMPLATES_FIXTURE = CollectiveCKTemplatesLayer()
CKTEMPLATES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CKTEMPLATES_FIXTURE,),
    name="CollectiveCKTemplatesLayer:Integration"
)
CKTEMPLATES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CKTEMPLATES_FIXTURE, z2.ZSERVER_FIXTURE),
    name="CollectiveCKTemplatesLayer:Functional"
)


CKTEMPLATES_ROBOT_TESTING = FunctionalTesting(
    bases=(CKTEMPLATES_FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE, z2.ZSERVER_FIXTURE),
    name="CKTEMPLATES_ROBOT_TESTING")

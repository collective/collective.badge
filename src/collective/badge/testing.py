from plone.app.testing import (PLONE_FIXTURE, IntegrationTesting,
                               PloneSandboxLayer, applyProfile)
from plone.testing import z2
from zope.configuration import xmlconfig


class CollectiveBadgeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.badge
        xmlconfig.file(
            'configure.zcml',
            collective.badge,
            context=configurationContext
        )

        z2.installProduct(app, 'collective.workspace')

    def testDownZope(self, app, configurationContext):
        z2.uninstallProduct(app, 'collective.workspace')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.badge:default')


COLLECTIVE_BADGE_FIXTURE = CollectiveBadgeLayer()
COLLECTIVE_BADGE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_BADGE_FIXTURE,),
    name="CollectiveBadgeLayer:Integration"
)

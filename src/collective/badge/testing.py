from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

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

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.badge:default')


COLLECTIVE_BADGE_FIXTURE = CollectiveBadgeLayer()
COLLECTIVE_BADGE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_BADGE_FIXTURE,),
    name="CollectiveBadgeLayer:Integration"
)

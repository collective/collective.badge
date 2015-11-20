from collective.badge.testing import COLLECTIVE_BADGE_INTEGRATION_TESTING
from plone import api
from plone.testing import z2
from plone.app.testing import SITE_OWNER_NAME
import unittest


class TestBadge(unittest.TestCase):
    layer = COLLECTIVE_BADGE_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        z2.login(self.app['acl_users'], SITE_OWNER_NAME)
        self.user1 = api.user.create(
            email='user1@example.com',
            username='user1',
            password='123'
        )
        self.badge = api.content.create(
            container=self.portal,
            type='Badge',
            id='test-badge',
        )

    def test_create_badge(self):
        pass

    def test_assign_badge_to_user(self):
        pass

    def test_remove_badge_from_user(self):
        pass

    def test_render_badge_view(self):
        pass

    def test_badges_for_user(self):
        pass

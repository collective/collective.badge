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
            title='Test Badge',
        )

    def test_create_badge(self):
        self.assertTrue('test-badge' in self.portal)
        badge = self.portal['test-badge']
        self.assertEquals('Badge', badge.portal_type)

    def test_render_badge_view(self):
        html = self.badge()
        self.assertTrue('Test Badge' in html)

    def test_assign_badge_to_user(self):
        badge = self.badge
        badge.assign_to_user('user1')
        self.assertTrue(badge.is_assigned_to_user('user1'))

        badge.remove_from_user('user1')
        self.assertFalse(badge.is_assigned_to_user('user1'))

    def test_list_active_users(self):
        badge = self.badge
        self.assertEqual(badge.list_active_users(), [])

        badge.assign_to_user('user1')
        self.assertEqual(badge.list_active_users(), ['user1'])

    def test_badges_for_user(self):
        from ..api import badges_for_user
        self.assertEquals(len(badges_for_user('user1')), 0)

        self.badge.assign_to_user('user1')
        self.assertEquals(len(badges_for_user('user1')), 1)

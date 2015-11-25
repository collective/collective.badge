from AccessControl import ClassSecurityInfo
from collective.workspace.interfaces import IWorkspace
from datetime import date
from ComputedAttribute import ComputedAttribute
from plone.dexterity.content import Item
from zope.interface import implementer
from .interfaces import IBadge


@implementer(IBadge)
class Badge(Item):

    security = ClassSecurityInfo()

    security.declarePrivate('workspace')
    def _workspace(self):
        return IWorkspace(self)
    workspace = ComputedAttribute(_workspace, 1)

    @security.private
    def assign_to_user(self, user_id, **kw):
        self.workspace.add_to_team(user_id, **kw)

    @security.private
    def remove_from_user(self, user_id):
        self.workspace[user_id].remove_from_team()

    @security.private
    def is_assigned_to_user(self, user_id):
        m = self.workspace.get(user_id)
        if m is None:
            return False
        today = date.today()
        if m.assigned > today:
            return False
        if m.expires and m.expires >= today:
            return False
        return True

    @security.private
    def list_active_users(self):
        today = date.today()
        users = []
        for m in self.workspace:
            if m.assigned > today:
                continue
            if m.expires and m.expires >= today:
                continue
            users.append(m.user)
        return users

from datetime import date

from collective.workspace.interfaces import IWorkspace
from collective.workspace.membership import ITeamMembership, TeamMembership
from collective.workspace.workspace import Workspace
from plone import api
from plone.app.z3cform.widget import DateFieldWidget
from plone.autoform import directives as form
from zope import schema
from zope.component import adapter
from zope.interface import implementer

from .interfaces import IBadge


def default_assigned_by():
    mtool = api.portal.get_tool('portal_membership')
    if not mtool.isAnonymousUser():
        member = mtool.getAuthenticatedMember()
        actor = member.getProperty('fullname')
        if not actor:
            actor = member.getProperty('id')
    else:
        actor = 'Nobody'
    if isinstance(actor, str):
        actor = actor.decode('utf8')
    return actor


class IBadgeMembership(ITeamMembership):

    # hide default workspace fields
    form.omitted('groups')
    form.omitted('position')

    assigned = schema.Date(
        title=u'Date Assigned',
        required=True,
        defaultFactory=date.today,
    )
    form.widget('assigned', DateFieldWidget)

    assigned_by = schema.TextLine(
        title=u'Assigned By',
        description=u'Enter your name or the person who approved adding '
                    u'this person to this badge.',
        required=False,
        defaultFactory=default_assigned_by,
    )

    expires = schema.Date(
        title=u'Expiration Date',
        required=False,
    )
    form.widget('expires', DateFieldWidget)

    notes = schema.Text(
        title=u'Notes',
        description=u"Optional. Enter any pertinent info about this "
                    u"person's badge record.",
        required=False,
    )


@implementer(IBadgeMembership)
class BadgeMembership(TeamMembership):
    _schema = IBadgeMembership

    def handle_added(self):
        """Ensure that default values are stored.
        """
        if 'assigned' not in self.__dict__:
            self.assigned = date.today()

        if 'assigned_by' not in self.__dict__:
            self.assigned_by = default_assigned_by()


@adapter(IBadge)
@implementer(IWorkspace)
class BadgeWorkspace(Workspace):
    """Custom workspace adapter for badges.
    """
    membership_schema = IBadgeMembership
    membership_factory = BadgeMembership

    # disable default collective.workspace groups
    available_groups = {}

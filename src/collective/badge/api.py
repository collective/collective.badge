from plone import api


def badges_for_user(user_id):
    """Returns a user's active badges.

    Only includes badges that have not expired.

    Sorted alphabetically.
    """
    catalog = api.portal.get_tool('portal_catalog')
    badges = []
    for brain in catalog.searchResults(
            portal_type='Badge',
            workspace_members=user_id,
            sort_on='sortable_title',
            ):
        badge = brain.getObject()
        if not badge.is_assigned_to_user(user_id):
            continue
        badges.append(badge)
    return badges


__all__ = ['badges_for_user']

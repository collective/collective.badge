.. image:: https://travis-ci.org/collective/collective.badge.svg?branch=master
    :target: https://travis-ci.org/collective/collective.badge

collective.badge
================

Introduction
------------

This package adds a content type for representing badges that can be assigned to users.

Each badge has an image and a roster (provided using collective.workspace) which includes:

- User
- Date Assigned
- Assigned By
- Expiration

The package is developed and tested on Plone 5.

An example of its use is on Plone.org, e.g. https://plone.org/profile/davisagli


Installation
------------

* Add collective.badge to your buildout eggs.
* Activate collective.badge in the 'Add-ons' section of Plone's Site Setup.


API
---

Assign a badge to a user::

	>>> badge.assign_to_user(user_id='admin')

Check if a badge is active for a user
(includes checking that the badge has not expired)::

    >>> badge.is_assigned_to_user(user_id='admin')
    True

List user ids of all active users for a badge::

    >>> badge.list_active_users()
    ['admin']

Remove a badge from a user::

    >>> badge.remove_from_user(user_id='admin')

Get a user's active badges (sorted alphabetically)::

    >>> from collective.badge.api import badges_for_user
    >>> badges_for_user(user_id='admin')
    [<Badge at /Plone/badges/awesome-badge>]

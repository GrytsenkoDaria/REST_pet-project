from django.db import models
from django.utils.translation import gettext as _


class Status(models.IntegerChoices):
    CREATED = (0, _('Created'))
    ACTIVE = (1, _('Active'))
    PAUSED = (2, _('Paused'))
    CLOSED = (3, _('Closed'))


class TaskStatus(models.IntegerChoices):
    TO_DO = (0, _('To do'))
    IN_PROGRESS = (1, _('In progress'))
    READY_FOR_REVIEW = (2, _('Ready for review'))
    REQUIRES_TESTING = (3, _('Requires testing'))
    IN_TESTING = (4, _('In testing'))
    DONE = (5, _('Done'))


class Role(models.IntegerChoices):
    ADMIN = (0, _('Admin'))
    MANAGER = (1, _('Manager'))
    USER = (2, _('User'))


class UserStatus(models.IntegerChoices):
    CREATED = (0, _('Created'))
    INVITED = (1, _('Invited'))
    ACTIVATED = (2, _('Activated'))
    ACTIVE = (3, _('Active'))
    BLOCKED = (4, _('Blocked'))
    DELETED = (5, _('Deleted'))

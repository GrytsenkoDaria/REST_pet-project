from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class Profile(models.Model):
    class Role(models.IntegerChoices):
        ADMIN = 0, _('Admin')
        MANAGER = 1, _('Manager')
        USER = 2, _('User')

    class Status(models.IntegerChoices):
        CREATED = 0, _('Created')
        INVITED = 1, _('Invited')
        ACTIVATED = 2, _('Activated')
        ACTIVE = 3, _('Active')
        BLOCKED = 4, _('Blocked')
        DELETED = 5, _('Deleted')

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    role = models.IntegerField(choices=Role.choices,)
    status = models.IntegerField(choices=Status.choices,)

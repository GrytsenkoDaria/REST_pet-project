from django.db import models
from django.conf import settings


class Profile(models.Model):
    class Role(models.IntegerChoices):
        ADMIN = 0, 'Admin'
        MANAGER = 1, 'Manager'
        USER = 2, 'User'

    class Status(models.IntegerChoices):
        CREATED = 0, 'Created'
        INVITED = 1, 'Invited'
        ACTIVATED = 2, 'Activated'
        ACTIVE = 3, 'Active'
        BLOCKED = 4, 'Blocked'
        DELETED = 5, 'Deleted'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    role = models.IntegerField(choices=Role.choices,)
    status = models.IntegerField(choices=Status.choices,)

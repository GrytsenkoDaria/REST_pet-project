from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    ADMIN = 0
    MANAGER = 1
    USER = 2
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (USER, 'User'),
    ]
    role = models.IntegerField(choices=ROLE_CHOICES,)

    CREATED = 0
    INVITED = 1
    ACTIVATED = 2
    ACTIVE = 3
    BLOCKED = 4
    DELETED = 5
    STATUS_CHOICES = [
        (CREATED, 'Created'),
        (INVITED, 'Invited'),
        (ACTIVATED, 'Activated'),
        (ACTIVE, 'Active'),
        (BLOCKED, 'Blocked'),
        (DELETED, 'Deleted'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES,)

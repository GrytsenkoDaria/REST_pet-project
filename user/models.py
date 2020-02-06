from django.db import models
from django.conf import settings
from choices import Role, UserStatus


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    role = models.IntegerField(choices=Role.choices,)
    status = models.IntegerField(choices=UserStatus.choices,)

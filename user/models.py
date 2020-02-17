from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

from django.contrib.auth.models import AbstractUser
from choices import Role, UserStatus


class User(AbstractUser):
    email = models.EmailField(unique=True,)
    role = models.IntegerField(choices=Role.choices, default=2)
    # default role 2 = User
    status = models.IntegerField(choices=UserStatus.choices, default=0)
    # default status 0 = Created


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

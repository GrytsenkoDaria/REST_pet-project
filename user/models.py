from django.db import models
from choices import Role, UserStatus
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True,)
    role = models.IntegerField(choices=Role.choices, default=2)
    # default role 2 = User
    status = models.IntegerField(choices=UserStatus.choices, default=0)
    # default status 0 = Created

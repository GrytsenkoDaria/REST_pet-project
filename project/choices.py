from django.db import models
from django.utils.translation import gettext as _


class Status(models.IntegerChoices):
    CREATED = (0, _('Created'))
    ACTIVE = (1, _('Active'))
    PAUSED = (2, _('Paused'))
    CLOSED = (3, _('Closed'))

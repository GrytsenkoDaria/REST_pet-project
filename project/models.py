from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class Project(models.Model):
    class Status(models.IntegerChoices):
        CREATED = (0, _('Created'))
        ACTIVE = (1, _('Active'))
        PAUSED = (2, _('Paused'))
        CLOSED = (3, _('Closed'))

    name = models.CharField(max_length=100)  # need to specify max_length?
    users = models.ManyToManyField(
        # why 'users' not 'user'? it is always singular
        'user.Profile',
        through='ProjectUser'
    )
    status = models.IntegerField(choices=Status.choices)

    def __str__(self):
        return self.name


class ProjectUser(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        'user.Profile',
        on_delete=models.CASCADE
    )
    is_ower = models.BooleanField(default=False)


class Release(models.Model):
    name = models.CharField(max_length=100)  # need to specify max_length?
    status = models.IntegerField(choices=Project.Status.choices)
    # can I adress to the Status in class Project above?
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    start_time = models.DateTimeField(auto_now=True)
    # should we set a start by 'auto_now' or let it be blank?
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name


class Sprint(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField(choices=Project.Status.choices)
    release = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name

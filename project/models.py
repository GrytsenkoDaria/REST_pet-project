from django.db import models
from .choices import Status


class Project(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(
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
    is_owner = models.BooleanField(default=False)


class Release(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=Status.choices)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name


class Sprint(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=Status.choices)
    release = models.ForeignKey(
        Release,
        on_delete=models.CASCADE
    )
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name

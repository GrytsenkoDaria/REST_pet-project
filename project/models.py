from django.db import models

from choices import Status


class Project(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(
        'user.User',
        through='ProjectUser',
        related_name='projects'
    )
    status = models.IntegerField(choices=Status.choices, default=0)

    def __str__(self):
        return self.name


class ProjectUser(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
    )
    is_owner = models.BooleanField(default=False)


class Release(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=Status.choices, default=0)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='releases'
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name


class Sprint(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=Status.choices, default=0)
    release = models.ForeignKey(
        Release,
        on_delete=models.CASCADE,
        related_name='sprints'
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name

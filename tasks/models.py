from django.db import models
from django.utils.translation import gettext as _


class Task(models.Model):
    class Status(models.IntegerChoices):
        TO_DO = (0, _('To do'))
        IN_PROGRESS = (1, _('In progress'))
        READY_FOR_REVIEW = (2, _('Ready for review'))
        REQUIRES_TESTING = (3, _('Requires testing'))
        IN_TESTING = (4, _('In testing'))
        DONE = (5, _('Done'))

    name = models.CharField(max_length=255)
    description = models.TextField()
    assignee = models.ForeignKey('user.Profile', on_delete=models.CASCADE)
    initiator = models.ForeignKey('user.Profile', on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status.choices, )
    project = models.ForeignKey('project.Project', on_delete=models.CASCADE)
    release = models.ForeignKey('project.Release', on_delete=models.CASCADE)
    sprint = models.ForeignKey('project.Sprint', on_delete=models.CASCADE)
    parent_task = models.ForeignKey(
        'self',
        null=True,
        on_delete=models.CASCADE
    )
    estimation = models.IntegerField(null=True)
    created = models.DateTimeField(blank=False)
    updated = models.DateTimeField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(
        'user.Profile',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created = models.DateTimeField()

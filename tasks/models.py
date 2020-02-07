from django.db import models
from choices import TaskStatus


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    assignee = models.ForeignKey(
        'user.Profile',
        on_delete=models.CASCADE,
        related_name='assigned_tasks'
    )
    initiator = models.ForeignKey(
        'user.Profile',
        on_delete=models.CASCADE,
        related_name='created_tasks'
    )
    status = models.IntegerField(choices=TaskStatus.choices)
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    release = models.ForeignKey(
        'project.Release',
        on_delete=models.CASCADE,
        related_name='tasks'
        )
    sprint = models.ForeignKey(
        'project.Sprint',
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    parent_task = models.ForeignKey(
        'self',
        null=True,
        on_delete=models.CASCADE,
        related_name='sub_tasks'
    )
    estimation = models.IntegerField(null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(
        'user.Profile',
        on_delete=models.CASCADE,
        related_name='created_comments'
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    created = models.DateTimeField()

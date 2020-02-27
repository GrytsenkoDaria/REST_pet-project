from django.db import models
from choices import TaskStatus


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    assignee = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='assigned_tasks',
        null=True,
        blank=True,
    )
    initiator = models.ForeignKey(
        'user.User',
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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='created_comments'
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    created = models.DateTimeField()

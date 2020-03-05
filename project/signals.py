from django.db.models.signals import post_save
from django.dispatch import receiver

from project.models import Project
from sandsiv_internship_project.tasks import send_mail_celery


@receiver(post_save, sender=Project)
def send_email_when_project_created(sender, created, **kwargs):
    obj = kwargs['instance']
    if created:
        send_mail_celery.delay(
            message=f'A new project {obj} was created!',
        )

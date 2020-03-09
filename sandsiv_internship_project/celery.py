from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'sandsiv_internship_project.settings'
)

app = Celery(
    'sandsiv_internship_project',
    broker='amqp://',
    backend='amqp://',
    )

app.config_from_object('django.conf:settings', namespace='CELERY')

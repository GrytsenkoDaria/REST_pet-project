from .celery import app
from django.core.mail import send_mail


@app.task
def send_mail_celery(message, *args):
    subject = 'New project!'
    from_email = 'from@example.com'
    recipient_list = ['to@example.com']

    send_mail(subject, message, from_email, recipient_list, )

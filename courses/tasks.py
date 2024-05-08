from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_message(email):
    send_mail(
        'Обновление курса',
        'Обновленился курс на котрый вы подписаны',
        settings.EMAIL_HOST_USER,
        email,

    )




from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import send_mail

from config import settings
from lms.models import Subscribe
from users.models import User


@shared_task
def send_message_about_changes(course_id):
    users = User.objects.all()

    for user in users:
        if Subscribe.objects.filter(course_id=course_id, owner=user).exists():
            send_mail(
                subject='Курс был изменен!',
                message='В курсе на который вы были подписаны произошли изменения',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email,],
            )




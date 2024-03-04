from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model

from celery import shared_task

from users.models import User


@shared_task
def deactivate_user():
    users = User.objects.filter(is_active=True, last_login__lte=timezone.now() - timedelta(days=30))
    for user in users:
        user.is_active = False
        user.save()

    # users.update(is_active=False)

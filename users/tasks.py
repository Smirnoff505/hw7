from datetime import datetime, timedelta

from users.models import User


def deactivate_user():

    delta = datetime.now() - timedelta(days=30)

    for user in User.objects.all():
        if user.last_login >= delta:
            user.is_active = False
            user.save()

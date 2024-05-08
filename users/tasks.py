import datetime

from celery import shared_task
from django.utils import timezone
from users.models import User

@shared_task(name='User date')
def user_data_task():
    # Получаем всех пользователей, которые не заходили в систему последние 30 дней
    users_to_update = User.objects.filter(last_login__lte=timezone.now() - timezone.timedelta(days=30))

    # Обновляем статус активного пользователя для тех, кто не заходил в систему последние 30 дней
    for user in users_to_update:
        user.is_active = False
        user.save()
        print(f'User {user.email} is deactivated')


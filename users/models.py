from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    avatar = models.ImageField(upload_to='avatars', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



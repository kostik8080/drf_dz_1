from django.contrib.auth.models import AbstractUser
from django.db import models

from courses.models import Course, Lesson

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='avatars', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payment(models.Model):
    PAYMENT_CHOICES = [('cash', 'Наличными'), ('card', 'Картой')]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    data_pay = models.DateTimeField(verbose_name='Дата оплаты', **NULLABLE)
    course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.CASCADE, **NULLABLE)
    lesson = models.ForeignKey(Lesson, verbose_name='Урок', on_delete=models.CASCADE, **NULLABLE)
    price = models.PositiveIntegerField(verbose_name='Цена', **NULLABLE)
    Payment_method = models.CharField(max_length=255, choices=PAYMENT_CHOICES, verbose_name='Способ оплаты', **NULLABLE)
    session_id = models.CharField(max_length=255, verbose_name='id сессии', **NULLABLE,
                                  help_text='Укажите id сессии')
    link = models.URLField(verbose_name='Ссылка на оплату', **NULLABLE, max_length=400,
                           help_text='Укажите ссылку на оплату')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Пользователь', **NULLABLE,
                             help_text='Укажите пользователя')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return self.price

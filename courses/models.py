from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название курса')
    photo = models.ImageField(upload_to='courses/', **NULLABLE, verbose_name='фото курса')
    description = models.TextField(verbose_name='описание курса')

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название урока')
    description = models.TextField(verbose_name='описание урока')
    photo = models.ImageField(upload_to='lessons/', **NULLABLE, verbose_name='фото урока')
    video = models.URLField(verbose_name='видео урока')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return self.title

import re

from rest_framework.serializers import ValidationError


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = "https://www.youtube.com/"
        try:
            tmp_value = value[self.field]
        except KeyError:
            raise ValidationError(f'Поле {self.field} не найдено в данных')

        if reg not in tmp_value:
            raise ValidationError('Недопустимый URL-адрес')


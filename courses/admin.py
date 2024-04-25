from django.contrib import admin

from courses.models import Course, Lesson
from users.models import User


admin.site.register(User)
admin.site.register(Course)
admin.site.register(Lesson)



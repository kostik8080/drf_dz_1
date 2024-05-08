from drf_yasg import openapi
from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from courses.models import Course, Lesson
from courses.validators import UrlValidator
from subscription.models import Subscription


class LessonsInfoField(serializers.JSONField):
    class Meta:
        swagger_schema_fields = {
            "type": 'array',
            "items": {
                "type": "object",
                "properties": {
                    'id': {'type': 'integer'},
                    'title': {'type':'string'},
                    'description': {'type':'string'},
                    'photo': {'type':'string'},
                    'video': {'type':'string'},
                    'course_id': {'type':'integer'},
                    'user_id': {'type':'integer'},
                }
            }


        }



class CourseSerializer(serializers.ModelSerializer):
    sub_title = serializers.SerializerMethodField()
    lsesons_count = serializers.SerializerMethodField()
    lessons_info = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'
        validators = [
            UrlValidator(field='url')
        ]

    @swagger_serializer_method(serializer_or_field=serializers.IntegerField)
    def get_lsesons_count(self, obj):
        lsesons_count = Lesson.objects.filter(course=obj).count()
        return lsesons_count

    @swagger_serializer_method(serializer_or_field=LessonsInfoField)
    def get_lessons_info(self, obj):
        lessons_info = Lesson.objects.filter(course=obj).values()
        return lessons_info

    def get_sub_title(self, obj):
        user = self.context['request'].user
        try:
            subscription = Subscription.objects.get(user=user, course=obj)
            return 'Вы подписаны на курс '
        except Subscription.DoesNotExist:
            return 'Вы не подписаны на курс '


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [
            UrlValidator(field='video')
        ]

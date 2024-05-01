from rest_framework import serializers

from courses.models import Course, Lesson
from courses.validators import UrlValidator
from subscription.models import Subscription


class CourseSerializer(serializers.ModelSerializer):
    sub_title = serializers.SerializerMethodField()
    lsesons_count = serializers.SerializerMethodField()
    lessons_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        validators = [
            UrlValidator(field='url')
        ]


    def get_lsesons_count(self, obj):
        lsesons_count = Lesson.objects.filter(course=obj).count()
        return lsesons_count

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

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     # Удаляем course_id и user_id из представления
    #     del data['course_id']
    #     del data['user_id']
    #     return data



class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [
            UrlValidator(field='video')
        ]

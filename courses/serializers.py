from rest_framework import serializers

from courses.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lsesons_count = serializers.SerializerMethodField()
    lessons_info = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = '__all__'

    def get_lsesons_count(self, obj):
        lsesons_count = Lesson.objects.filter(course=obj).count()
        return lsesons_count

    def get_lessons_info(self, obj):
        lessons_info = Lesson.objects.filter(course=obj).values()
        return lessons_info


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

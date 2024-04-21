from django.shortcuts import render
from rest_framework.viewsets import ViewSet, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from courses.models import Course, Lesson
from courses.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ViewSet):

    def list(self, request):
        """
        отображение списка сущностей, HTTP-метод GET.
        """
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        создание сущности, HTTP-метод POST.
        """

        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        """
        отображение сущности, HTTP-метод GET.
        """

        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        обновление сущности, HTTP-метод PUT.
        """

        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        """
        удаление сущности, HTTP-метод DELETE.
        """

        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        course.delete()
        return Response(status=204)


class LessonCreateAPIView(generics.CreateAPIView):
    """Создание нового урока"""
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    "Список всех уроков"
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Получение урока по id"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Обновление урока по id"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDeleteAPIView(generics.DestroyAPIView):
    """Удаление урока по id"""
    queryset = Lesson.objects.all()


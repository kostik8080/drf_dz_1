from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ViewSet, generics, ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from courses.models import Course, Lesson
from courses.paginators import CoursePagination, LessonPagination
from courses.permissions import IsModer, IsOwner
from courses.serializers import CourseSerializer, LessonSerializer
from courses.tasks import send_message
from subscription.models import Subscription


class CourseViewSet(ModelViewSet):
    """Список курсов. Создание, редактирование, удаление."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePagination

    def perform_create(self, serializer):
        """
        Создание пользователя по умодчанию кто авторизован.
        """
        course = serializer.save()
        course.user = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~IsModer, IsAdminUser,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (~IsModer | ~IsAdminUser | IsOwner,)
        return super().get_permissions()


    def perform_update(self, serializer):
        course = serializer.save()
        subscription = Subscription.objects.filter(course=course)
        if subscription:
            subscription_email = []
            for subscript in subscription:
                subscription_email.append(subscript.user.email)
                print(subscript.user.email)
                print(subscription_email)
            send_message.delay(subscription_email)

        course.save()





class LessonCreateAPIView(generics.CreateAPIView):
    """Создание нового урока"""
    serializer_class = LessonSerializer

    permission_classes = (~IsModer, ~IsAdminUser, IsAuthenticated,)

    def perform_create(self, serializer):
        """
        Создание пользователя по умодчанию кто авторизован.
        """
        lesson = serializer.save()
        lesson.user = self.request.user
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    "Список всех уроков"
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = LessonPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Получение урока по id"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModer | IsOwner,)


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Обновление урока по id"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModer | IsOwner,)


class LessonDeleteAPIView(generics.DestroyAPIView):
    """Удаление урока по id"""
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsOwner | ~IsModer | ~IsAdminUser,)

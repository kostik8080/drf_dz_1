from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase

from subscription.models import Subscription
from users.models import User
from .models import Lesson, Course


class LessonTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='testov@mail.ru')

        self.course = Course.objects.create(title='testCourse', description='testCourse', user=self.user)
        self.lesson = Lesson.objects.create(title='test', description='test', user=self.user, course=self.course)
        #self.lesson = Lesson.objects.create(title='test2', description='test2', user=self.user, course=self.course)
        # self.subscription = Subscription.objects.create(lesson=self.course, user=self.user)

        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('courses:lesson_detail', kwargs={'pk': self.lesson.pk})
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['title'], self.lesson.title)
        self.assertEqual(data['description'], self.lesson.description)

    def test_lesson_list(self):
        url = reverse('courses:lesson_list')
        lesson = Lesson.objects.all().count()
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(lesson, self.client.get(url).json()['count'])
        response = self.client.get(url, {'page_size': 1})
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(lesson, data['count'])




    def test_lesson_create(self):
        url = reverse('courses:lesson_create')
        data = {
            'title': 'Знакомство с программированием',
            'description': 'урок 1 посвященный программированию',
            #'video': 'hjdjdjdjdjdjd'
            'video': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)
        self.assertEqual(self.user.pk, response.json().get('user'))
        self.assertEqual(data.get('video'), response.json().get('video'))
        with self.assertRaises(Lesson.DoesNotExist):
            Lesson.objects.get(title='Знакомство  программированием')


    def test_lesson_update(self):
        url = reverse('courses:lesson_update', kwargs={'pk': self.lesson.pk})
        data = {
            'title': 'Знакомство с программированием python',
            'description': 'урок 2 посвященный программированию',
            #'video': 'hjdjdjdjdjdjd'
            'video': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), 'Знакомство с программированием python')
        self.assertEqual(data.get('description'), 'урок 2 посвященный программированию')
        self.assertEqual(self.user.pk, response.json().get('user'))
        self.assertEqual(data.get('video'), response.json().get('video'))


    def test_lesson_delete(self):
        url = reverse('courses:lesson_delete', kwargs={'pk': self.lesson.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)



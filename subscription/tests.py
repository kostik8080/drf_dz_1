from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase

from courses.models import Course, Lesson
from subscription.models import Subscription
from users.models import User


class LessonTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='testov@mail.ru')

        self.course = Course.objects.create(title='testCourse', description='testCourse', user=self.user)


        self.client.force_authenticate(user=self.user)

    def test_subscrpition_create(self):
        data = {
            'course_id': self.course.id,


        }
        url = reverse('subscription:subscriptions')

        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('message'), 'подписка добавлена')

        response = self.client.post(url, data)
        self.assertEqual(response.json().get('message'), 'подписка удалена')
        with self.assertRaises(Subscription.DoesNotExist):
            Subscription.objects.get(course_id=self.course.id)


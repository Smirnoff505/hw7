import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            id=1,
            email='test@user.ru',
            password='test'

        )
        self.course = Course.objects.create(
            id=1,
            title='test category field'
        )

        self.lesson = Lesson.objects.create(
            id=1,
            title='test',
            course=self.course,
            owner=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_get_list(self):
        """Тест на получение списка уроков"""

        response = self.client.get(
            reverse('lms:lesson-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 1,
                        "title": "test",
                        "description": None,
                        "preview": None,
                        "link_video": None,
                        "course": self.course.id,
                        "owner": self.user.id
                    }
                ]
            }
        )

    def test_lesson_detail(self):
        """Тест для просмотра урока"""

        response = self.client.get(
            reverse('lms:lesson-detail', kwargs={'pk': 1}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "title": "test",
                "description": None,
                "preview": None,
                "link_video": None,
                "course": self.course.id,
                "owner": self.user.id
            }
        )

    # def test_lesson_update(self):
    #     """Тест для обновления урока"""
    #
    #     data = {
    #         'description': 'test'
    #     }
    #
    #     response = self.client.patch(
    #         reverse('lms:lesson-update', kwargs={'pk': 1}),
    #         data=data
    #     )
    #
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )

    def test_lesson_delete(self):
        """Тест удаления урока"""

        response = self.client.delete(
            reverse('lms:lesson-delete', kwargs={'pk': 1})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    # def test_lesson_create(self):
    #     """Тест для создания урока"""
    #
    #     data = {
    #         'title': 'test create',
    #         'description': 'test create',
    #         'course': self.course.id,
    #         'owner': self.user.id
    #     }
    #     response = self.client.post(
    #         reverse('lms:lesson-create'),
    #         data=data,
    #     )
    #
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_201_CREATED
    #     )
    #
    # self.assertEqual(
    #     response.json(),
    #     {
    #         "id": 2,
    #         "title": "test create",
    #         "description": "test create",
    #         "preview": None,
    #         "link_video": None,
    #         "course": self.course.id,
    #         "owner": self.user.id,
    #     }
    # )

    def tearDown(self):
        pass


class SubscribeTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            id=1,
            email='test@user.ru',
            password='test'

        )
        self.course = Course.objects.create(
            id=1,
            title='test1'
        )

        self.client.force_authenticate(user=self.user)

    def test_subscribe(self):
        """Тест включения/отключения подписки"""

        response = self.client.post(
            reverse('lms:subscribe', kwargs={'pk': 1})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'message': 'подписка добавлена'}
        )

    def tearDown(self):
        pass

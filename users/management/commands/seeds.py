from django.core.management import BaseCommand

from lms.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):

    def handle(self, *args, **options):

        courses_list = [
            {"title": "Курс Python-develop", "description": "Курс для Python разработчиков"},
            {"title": "Курс Java-develop", "description": "Курс для Java разработчиков"},
            {"title": "Курс Go-develop", "description": "Курс для Go разработчиков"},
            {"title": "Курс для фронтенд разработчиков", "description": "Курс CSS и JavaScript"}
        ]

        for course in courses_list:
            Course.objects.create(**course)

        lessons_list = [
            {"title": "Основы разработки Python", "description": "Основы языка Python", "course_id": 1},
            {"title": "Python практика", "description": "Домашнее задание", "course_id": 1},
            {"title": "Java практика", "description": "Домашнее задание", "course_id": 2}
        ]

        for lesson in lessons_list:
            Lesson.objects.create(**lesson)

        users_list = [
            {"email": "test@ya.ru", "password": "12345", "first_name": "Dan", "last_name": "First"},
            {"email": "neadmin@ya.ru", "password": "12345", "first_name": "John", "last_name": "Second"},
            {"email": "alex@ya.ru", "password": "12345", "first_name": "Alex", "last_name": "Third"}
        ]

        for user in users_list:
            User.objects.create(**user)

        payment_list = [
            {"payment_method": 1, "owner_id": 1, "paid_course_id": 1},
            {"payment_method": 2, "owner_id": 2, "paid_course_id": 2},
            {"payment_method": 1, "owner_id": 3, "paid_lesson_id": 1}
        ]

        for payment in payment_list:
            Payment.objects.create(**payment)

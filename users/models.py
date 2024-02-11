from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=35, verbose_name='телефон', blank=True, null=True)
    city = models.CharField(max_length=35, verbose_name='город', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):

    STATUS_CHOICES = [
        (1, 'Наличные'),
        (2, 'Перевод'),
    ]

    owner = models.ForeignKey('User', on_delete=models.DO_NOTHING, verbose_name='пользователь', related_name='owner')
    paid_course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name='оплата курса',
                                    related_name='paid_course', blank=True, null=True)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, verbose_name='оплата урока',
                                    related_name='paid_lesson', blank=True, null=True)

    date_of_payment = models.DateTimeField(auto_now_add=True, verbose_name='дата платежа')
    payment_amount = models.FloatField(verbose_name='сумма')
    payment_method = models.SmallIntegerField(choices=STATUS_CHOICES, default=1, verbose_name='метод оплаты')

    def __str__(self):
        return f'{self.owner}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'

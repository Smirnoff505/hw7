from django.db import models

from config import settings


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name='название')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    preview = models.ImageField(upload_to='course/', blank=True, null=True, verbose_name='превью')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='название')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    preview = models.ImageField(upload_to='lesson/', blank=True, null=True, verbose_name='превью')
    link_video = models.TextField(unique=True, verbose_name='ссылка на видео', blank=True, null=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscribe(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                              verbose_name='владелец')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, related_name='курс')
    subscription_activity = models.BooleanField(default=False, verbose_name='активность подписки')

    def __str__(self):
        return f'{self.owner}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

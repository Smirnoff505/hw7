from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name='название')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    preview = models.ImageField(upload_to='course/', blank=True, null=True, verbose_name='превью')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='название')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    preview = models.ImageField(upload_to='lesson/', blank=True, null=True, verbose_name='превью')
    link_video = models.SlugField(unique=True, verbose_name='ссылка на видео')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'



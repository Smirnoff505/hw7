from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.openapi import Schema, TYPE_OBJECT
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics, status

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from lms.models import Course, Lesson, Subscribe
from lms.paginators import LmsPaginator
from lms.permissions import IsModerator, IsOwner
from lms.serializes import CourseSerialize, LessonSerialize, SubscribeSerialize
from lms.tasks import send_message_about_changes


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerialize
    queryset = Course.objects.all()
    pagination_class = LmsPaginator

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        course_id = self.kwargs.get('pk')  # Извлечение идентификатора курса из URL
        update_course = serializer.save(course_id=course_id)
        send_message_about_changes.delay(update_course.id)  # Передача идентификатора объекта

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'partial_update':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in self.permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerialize
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerialize
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LmsPaginator


class LessonDetailAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerialize
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerialize
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class SubscribeView(APIView):
    serializer_class = CourseSerialize
    queryset = Subscribe.objects.all()

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="подписка добавлена или подписка удалена",
                examples={
                    "application/json": {
                        "message": "подписка добавлена",
                    }
                }
            )
        }
    )
    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = kwargs.get('pk')
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscribe.objects.filter(owner=user, course=course_item).first()

        if subs_item:
            # Если подписка уже есть, отменяем её
            subs_item.delete()
            message = 'подписка удалена'
        else:
            # Если подписки нет, создаем новую
            Subscribe.objects.create(owner=user, course=course_item, subscription_activity=True)
            message = 'подписка добавлена'

        return Response({"message": message})


class SubscribeListAPIView(generics.ListAPIView):
    serializer_class = SubscribeSerialize
    queryset = Subscribe.objects.all()

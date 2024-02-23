from django.urls import path

from lms.apps import LmsConfig
from rest_framework.routers import DefaultRouter

from lms.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonDetailAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, SubscribeView, SubscribeListAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('lesson/list/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lesson/<int:pk>/detail/', LessonDetailAPIView.as_view(), name='lesson-detail'),
                  path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

                  path('courses/<int:pk>/subscribe/', SubscribeView.as_view(), name='subscribe'),
                  path('subscribe/list/', SubscribeListAPIView.as_view(), name='subscribe-list')

              ] + router.urls

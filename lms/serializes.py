from rest_framework import serializers

from lms.models import Course, Lesson, Subscribe
from lms.validators import LinkVideoValidator


class LessonSerialize(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkVideoValidator(field='link_video')]


class SubscribeSerialize(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'


class CourseSerialize(serializers.ModelSerializer):
    subscribe = serializers.SerializerMethodField()
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerialize(source='course', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        if obj.course.all().count():
            return obj.course.all().count()
        return 0

    def get_subscribe(self, obj):
        subscribe = Subscribe.objects.filter(course=obj.pk, owner=self.context.get('request').user.pk)
        if subscribe.exists():
            return True
        else:
            return False

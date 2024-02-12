from rest_framework import serializers

from lms.models import Course, Lesson


class LessonSerialize(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerialize(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerialize(source='course', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        if obj.course.all().count():
            return obj.course.all().count()
        return 0




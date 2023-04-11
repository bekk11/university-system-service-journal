from rest_framework import serializers

from apps.course.serializers.course_serializer import CourseSerializer
from apps.timetable.models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Schedule
        fields = '__all__'

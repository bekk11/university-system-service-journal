import requests
from rest_framework import serializers

from apps.course.models import Course
from apps.subject.serializers.subject_serializer import SubjectSerializer
from config.settings import AUTHENTICATION_SERVICE


class CourseSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()

    teacher_id = serializers.SerializerMethodField('get_teacher_name')

    class Meta:
        model = Course
        fields = [
            'id',
            'group_id',
            'subject',
            'credits',
            'teacher_id',
            'semester',
        ]

    def get_teacher_name(self, obj):
        res = requests.get(f'{AUTHENTICATION_SERVICE}/apps/teacher/info/{obj.teacher_id}')
        return res.json()


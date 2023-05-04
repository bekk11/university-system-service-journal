from rest_framework import serializers

from apps.absent.models import Absent


class AbsentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absent
        fields = [
            'id',
            'journal',
            'student_id',
            'date',
            'schedule',
        ]

from rest_framework.generics import ListAPIView

from apps.timetable.models import Schedule
from apps.timetable.serializers.schedule_serializer import ScheduleSerializer


class ListSchedule(ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    filterset_fields = ['group_id', 'day', 'time', 'building', 'course', 'room']

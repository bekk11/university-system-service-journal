from rest_framework.generics import ListAPIView

from apps.absent.models import Absent
from apps.absent.serializers.absent_serializer import AbsentSerializer


class ListAbsents(ListAPIView):
    queryset = Absent.objects.all()
    serializer_class = AbsentSerializer
    filterset_fields = ('journal', 'student_id', 'date', 'schedule')

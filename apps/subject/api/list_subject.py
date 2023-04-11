from rest_framework.generics import ListAPIView

from apps.subject.models import Subject
from apps.subject.serializers.subject_serializer import SubjectSerializer


class ListSubject(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

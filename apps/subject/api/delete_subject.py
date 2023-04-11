from rest_framework.generics import UpdateAPIView, DestroyAPIView

from apps.subject.models import Subject
from apps.subject.serializers.subject_serializer import SubjectSerializer


class DeleteSubject(DestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

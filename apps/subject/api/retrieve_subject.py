from rest_framework.generics import RetrieveAPIView

from apps.subject.models import Subject
from apps.subject.serializers.subject_serializer import SubjectSerializer


class RetrieveSubject(RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

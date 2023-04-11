from rest_framework.generics import UpdateAPIView

from apps.subject.models import Subject
from apps.subject.serializers.subject_serializer import SubjectSerializer


class UpdateSubject(UpdateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

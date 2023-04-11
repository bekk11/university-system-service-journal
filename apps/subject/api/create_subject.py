from rest_framework.generics import CreateAPIView

from apps.subject.models import Subject
from apps.subject.serializers.subject_serializer import SubjectSerializer


class CreateSubject(CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

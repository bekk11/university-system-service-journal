from rest_framework.generics import ListAPIView

from apps.course.models import Course
from apps.course.serializers.course_serializer import CourseSerializer


class ListCourse(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_fields = ['group_id', 'semester']

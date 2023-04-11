from rest_framework.generics import RetrieveAPIView

from apps.course.models import Course
from apps.course.serializers.course_serializer import CourseSerializer


class RetrieveCourse(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

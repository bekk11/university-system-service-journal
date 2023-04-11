from rest_framework.generics import UpdateAPIView

from apps.course.models import Course
from apps.course.serializers.course_serializer import CourseSerializer


class UpdateCourse(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

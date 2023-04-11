from rest_framework.generics import CreateAPIView

from apps.course.models import Course
from apps.course.serializers.course_serializer import CourseSerializer


class CreateCourse(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

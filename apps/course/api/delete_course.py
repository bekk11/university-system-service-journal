from rest_framework.generics import DestroyAPIView

from apps.course.models import Course
from apps.course.serializers.course_serializer import CourseSerializer


class DeleteCourse(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

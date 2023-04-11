from django.contrib import admin

from apps.course.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'group_id',
        'subject',
        'credits',
        'teacher_id',
        'semester',
    ]

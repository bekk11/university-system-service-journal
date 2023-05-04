from django.contrib import admin

from apps.absent.models import Absent


@admin.register(Absent)
class AbsentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'journal',
        'student_id',
        'date',
        'schedule',
    ]

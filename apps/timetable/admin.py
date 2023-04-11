from django.contrib import admin

from apps.timetable.models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'group_id',
        'day',
        'time',
        'course',
        'building',
        'room',
    ]
    list_filter = ('day',)

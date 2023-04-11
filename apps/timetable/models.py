from django.db import models

from apps.course.models import Course


class Schedule(models.Model):
    DAY_CHOICE = [
        ['MONDAY', 'MONDAY'],
        ['TUESDAY', 'TUESDAY'],
        ['WEDNESDAY', 'WEDNESDAY'],
        ['THURSDAY', 'THURSDAY'],
        ['FRIDAY', 'FRIDAY'],
        ['SATURDAY', 'SATURDAY'],
        ['SUNDAY', 'SUNDAY'],
    ]

    TIME_CHOICE = [
        ["08:00-08:50", "08:00-08:50"],
        ["09:00-09:50", "09:00-09:50"],
        ["10:00-10:50", "10:00-10:50"],
        ["11:00-11:50", "11:00-11:50"],
        ["12:00-12:50", "12:00-12:50"],
        ["13:00-13:50", "13:00-13:50"],
        ["14:00-14:50", "14:00-14:50"],
        ["15:00-15:50", "15:00-15:50"],
        ["16:00-16:50", "16:00-16:50"],
        ["17:00-17:50", "17:00-17:50"],
        ["18:00-18:50", "18:00-18:50"],
        ["19:00-19:50", "19:00-19:50"],
        ["20:00-20:50", "20:00-20:50"],
        ["21:00-21:50", "21:00-21:50"],
    ]

    BUILDING_CHOICE = [
        ['A', 'A'],
        ['B', 'B'],
        ['C', 'C'],
        ['D', 'D'],
    ]

    group_id = models.BigIntegerField(null=False)
    day = models.CharField(max_length=25, choices=DAY_CHOICE)
    time = models.CharField(max_length=25, choices=TIME_CHOICE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    building = models.CharField(max_length=15, choices=BUILDING_CHOICE, null=True, blank=True, default=None)
    room = models.CharField(max_length=15, null=True, blank=True, default=None)

    def __str__(self):
        return self.course.subject.name

    class Meta:
        db_table = 'schedule'
        ordering = ['time', ]

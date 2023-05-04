import datetime

from django.db import models

from apps.journal.models import Journal
from apps.timetable.models import Schedule


class Absent(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    student_id = models.BigIntegerField(null=False)
    date = models.DateField(default=datetime.date.today())
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{}'.format(self.date)

    class Meta:
        db_table = 'absent'

from django.db import models

from apps.subject.models import Subject


class Course(models.Model):
    group_id = models.BigIntegerField(null=False, blank=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    credits = models.IntegerField(null=True, blank=True)
    teacher_id = models.BigIntegerField(null=True, blank=True)
    semester = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return self.subject.name

    class Meta:
        db_table = 'course'
        ordering = ['subject__name', 'semester']

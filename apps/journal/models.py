from django.db import models


class Journal(models.Model):
    group_id = models.BigIntegerField(null=False)

    class Meta:
        db_table = 'journal'

    def __str__(self):
        return '{}'.format(self.group_id)

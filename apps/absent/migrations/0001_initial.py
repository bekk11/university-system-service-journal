# Generated by Django 4.1.4 on 2023-05-04 11:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('timetable', '0002_schedule_building_schedule_room'),
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.BigIntegerField()),
                ('date', models.DateField(default=datetime.date(2023, 5, 4))),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.journal')),
                ('schedule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='timetable.schedule')),
            ],
            options={
                'db_table': 'absent',
            },
        ),
    ]

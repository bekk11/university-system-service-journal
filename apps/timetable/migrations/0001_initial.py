# Generated by Django 4.1.4 on 2023-04-06 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0004_alter_course_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.BigIntegerField()),
                ('day', models.CharField(choices=[['MONDAY', 'MONDAY'], ['TUESDAY', 'TUESDAY'], ['WEDNESDAY', 'WEDNESDAY'], ['THURSDAY', 'THURSDAY'], ['FRIDAY', 'FRIDAY'], ['SATURDAY', 'SATURDAY'], ['SUNDAY', 'SUNDAY']], max_length=25)),
                ('time', models.CharField(choices=[['08:00-08:50', '08:00-08:50'], ['09:00-09:50', '09:00-09:50'], ['10:00-10:50', '10:00-10:50'], ['11:00-11:50', '11:00-11:50'], ['12:00-12:50', '12:00-12:50'], ['13:00-13:50', '13:00-13:50'], ['14:00-14:50', '14:00-14:50'], ['15:00-15:50', '15:00-15:50'], ['16:00-16:50', '16:00-16:50'], ['17:00-17:50', '17:00-17:50'], ['18:00-18:50', '18:00-18:50'], ['19:00-19:50', '19:00-19:50'], ['20:00-20:50', '20:00-20:50'], ['21:00-21:50', '21:00-21:50']], max_length=25)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
            options={
                'db_table': 'schedule',
                'ordering': ['time'],
            },
        ),
    ]

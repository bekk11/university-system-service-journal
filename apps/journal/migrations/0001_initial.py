# Generated by Django 4.1.4 on 2023-05-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'journal',
            },
        ),
    ]

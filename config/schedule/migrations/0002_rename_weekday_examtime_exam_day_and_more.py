# Generated by Django 4.1.3 on 2022-12-15 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examtime',
            old_name='WeekDay',
            new_name='exam_day',
        ),
        migrations.RenameField(
            model_name='examtime',
            old_name='class_time',
            new_name='exam_time',
        ),
    ]

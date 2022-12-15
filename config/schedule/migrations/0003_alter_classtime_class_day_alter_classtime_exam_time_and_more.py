# Generated by Django 4.1.3 on 2022-12-15 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_rename_weekday_examtime_exam_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtime',
            name='class_day',
            field=models.ManyToManyField(related_name='class_time', to='schedule.weekday', verbose_name='روز کلاس'),
        ),
        migrations.AlterField(
            model_name='classtime',
            name='exam_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_time', to='schedule.examtime', verbose_name='زمان امتحان'),
        ),
        migrations.AlterField(
            model_name='examtime',
            name='exam_day',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='exam_time', to='schedule.weekday', verbose_name='روز امتحان'),
        ),
        migrations.AlterField(
            model_name='examtime',
            name='exam_time',
            field=models.TimeField(verbose_name='ساعت امتحان'),
        ),
    ]
# Generated by Django 4.1.3 on 2022-12-15 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_alter_examtime_exam_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='classtime',
            name='exam_day',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='exam_time', to='schedule.weekday', verbose_name='روز امتحان'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classtime',
            name='exam_time',
            field=models.TimeField(verbose_name='ساعت امتحان'),
        ),
        migrations.DeleteModel(
            name='ExamTime',
        ),
    ]
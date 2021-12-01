# Generated by Django 3.2.6 on 2021-11-30 15:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customAdmin', '0011_alter_employeeattendance_timein'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeattendance',
            name='timein',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='employeeattendance',
            name='timeout',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]

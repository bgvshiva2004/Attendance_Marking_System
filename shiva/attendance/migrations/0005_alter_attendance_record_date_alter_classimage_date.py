# Generated by Django 4.2.6 on 2023-10-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_attendance_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance_record',
            name='date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='classimage',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]

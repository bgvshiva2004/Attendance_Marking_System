# Generated by Django 4.2.6 on 2023-10-16 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classimage',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

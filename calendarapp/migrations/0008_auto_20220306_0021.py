# Generated by Django 3.1.13 on 2022-03-06 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0007_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='atraso',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='eventmember',
            name='atraso',
            field=models.IntegerField(default=0),
        ),
    ]

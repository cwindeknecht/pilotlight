# Generated by Django 2.0.2 on 2018-10-19 19:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pilot', '0009_auto_20181019_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='date',
            field=models.DateTimeField(default='  ', verbose_name=datetime.datetime(2018, 10, 19, 19, 13, 45, 734809, tzinfo=utc)),
        ),
    ]

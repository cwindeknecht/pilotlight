# Generated by Django 2.0.2 on 2018-10-19 18:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pilot', '0002_auto_20181019_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 10, 19, 18, 8, 5, 23651, tzinfo=utc)),
        ),
    ]
# Generated by Django 2.1.7 on 2019-03-08 04:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='summary',
            field=models.CharField(default=datetime.datetime(2019, 3, 8, 4, 8, 11, 456429, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
    ]

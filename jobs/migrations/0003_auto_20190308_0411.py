# Generated by Django 2.1.7 on 2019-03-08 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]

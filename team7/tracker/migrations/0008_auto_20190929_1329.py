# Generated by Django 2.2.5 on 2019-09-29 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_auto_20190929_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='end',
            field=models.DateTimeField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='start',
            field=models.DateTimeField(),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='project_images'),
        ),
    ]
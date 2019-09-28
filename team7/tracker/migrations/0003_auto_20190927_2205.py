# Generated by Django 2.2.5 on 2019-09-27 22:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20190927_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='man_hours',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_auto_20190929_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='start',
            field=models.DateField(),
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-29 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20190928_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]

from django.db import models
from django.core.validators import MinValueValidator
from datetime import date
from django.core.exceptions import ValidationError


class Project(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    man_hours = models.IntegerField(validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to=u'project_images')
    owner = models.ForeignKey(
        'auth.User', related_name='projects', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return '{0}'.format(self.name)


class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    man_hours = models.IntegerField(validators=[MinValueValidator(1)])
    project = models.ForeignKey(
        Project, related_name='tasks', on_delete=models.CASCADE, null=False)
    assignee = models.ForeignKey(
        'auth.User', related_name='assignee', on_delete=models.CASCADE, null=False)
    start = models.DateField()
    end = models.DateField()

    def clean(self):
        if self.end < self.start:
            raise ValidationError("End date must be after start date.")

    def __str__(self):
        return '{0}'.format(self.name)

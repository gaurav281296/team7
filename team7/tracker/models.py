from django.db import models
from django.core.validators import MinValueValidator

class Project(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    man_hours = models.IntegerField(validators=[MinValueValidator(1)])

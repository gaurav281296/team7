from django.contrib.auth.models import User
from .models import Project, Task
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description',
                  'man_hours', 'image', 'owner']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description',
                  'man_hours', 'project', 'assignee', 'start', 'end']


class ProjectTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['tasks']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

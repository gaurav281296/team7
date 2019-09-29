from django.shortcuts import render
from rest_framework.response import Response
from tracker.models import Project, Task
from django.contrib.auth.models import User
from tracker.serializers import ProjectSerializer, UserSerializer, TaskSerializer, ProjectTaskSerializer
from rest_framework import generics
from rest_framework.decorators import api_view


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


@api_view(['GET'])
def project_tasks(request, pk):
    projects = Project.objects.all()
    serializer = ProjectTaskSerializer(projects, many=True)
    task_keys = dict(serializer.data[0])['tasks']
    tasks = Task.objects.filter(id__in=task_keys)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

from django.shortcuts import render
from rest_framework.response import Response
from tracker.models import Project, Task
from django.contrib.auth.models import User
from tracker.serializers import ProjectSerializer, UserSerializer, TaskSerializer, ProjectTaskSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status


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
def project_task(request, pk):
    projects = Project.objects.filter(id=pk)
    serializer = ProjectTaskSerializer(projects, many=True)
    try:
        task_keys = dict(serializer.data[0])['tasks']
    except Exception as e:
        return Response("Invalid Project")
    tasks = Task.objects.filter(id__in=task_keys)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def project_task_detail(request, pk, tk):
    projects = Project.objects.filter(id=pk)
    serializer = ProjectTaskSerializer(projects, many=True)
    try:
        task_keys = dict(serializer.data[0])['tasks']
    except Exception as e:
        return Response("Invalid Project")

    if tk in task_keys:
        try:
            task = Task.objects.filter(id=tk)
        except Snippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = TaskSerializer(task, many=True)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response("Task does not belong to project")

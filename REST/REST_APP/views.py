from django.shortcuts import render
from .serializers import TaskSerializers
from .models import Task
from rest_framework import viewsets
# Create your views here.

class TaskViewset(viewsets.ModelViewSet):
    queryset=Task.objects.all().order_by('date_created')
    serializer_class=TaskSerializers
class DueTaskViewset(viewsets.ModelViewSet):
    queryset=Task.objects.all().order_by('date_created').filter(completed=False)
    serializer_class=TaskSerializers


class CompletedTaskViewset(viewsets.ModelViewSet):
    queryset=Task.objects.all().order_by('date_created').filter(completed=True)
    serializer_class=TaskSerializers
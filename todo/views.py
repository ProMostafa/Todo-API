from django.shortcuts import render
from .models import Todo 
from .serializers import TodoSerializer

from rest_framework import viewsets

# Create your views here.

class ListTodoViewSet(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

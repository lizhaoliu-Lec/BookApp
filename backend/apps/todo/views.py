from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from ..todo.models import Todo
from ..todo.serializers import TodoSetSerializer


# Create your views here.
class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSetSerializer


# from rest_framework import serializers
# from ..todo.models import Todo
# from ..todoSet.serializer import TodoSetSerializer
#
#
# class TodoSerializer(serializers):
#     # deadline = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
#     # belongTodoSet = TodoSetSerializer(many=True)
#
#     class Meta:
#         model = Todo
#         fields = ['id', 'name', 'attendTimes', 'quitTimes', 'totalTime', 'deadline', 'type', 'loopMode', 'expectedTime',
#                   'belongTodoSet']

from rest_framework.serializers import ModelSerializer
from ..todo.models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"


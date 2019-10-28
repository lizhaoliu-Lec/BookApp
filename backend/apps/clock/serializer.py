from rest_framework import serializers
from ..todo.serializers import TodoSerializer
from ..clock.models import Clock


class ClockSerializer(serializers):
    startTime = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    endTime = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    belongTodo = TodoSerializer(many=True)

    class Meta:
        model = Clock
        field = "__all__"



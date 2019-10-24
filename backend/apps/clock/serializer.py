from rest_framework import serializers
from ..todo.serializers import TodoSetSerializer
from ..clock.models import Clock


class ClockSerializer(serializers):
    startTime = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    endTime = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    belongTodo = TodoSetSerializer(many=True)

    class Meta:
        model = Clock
        field = "__all__"



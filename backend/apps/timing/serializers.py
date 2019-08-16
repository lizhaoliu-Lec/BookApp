from rest_framework import serializers

from . import models
from ..user.serializer import UserSerializer


class TimingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TimingRecord
        fields = ['id', 'time', 'remark', 'type', 'start_time', 'end_time']

    id = serializers.IntegerField(read_only=True)
    type = serializers.CharField(source='get_type_display')
    start_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    end_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')


class TimingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TimingPlan
        fields = ['id', 'user', 'description']

    id = serializers.IntegerField(read_only=True)


class TimingGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TimingGroup
        fields = ['id', 'user', 'description']

    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(many=True, read_only=True)

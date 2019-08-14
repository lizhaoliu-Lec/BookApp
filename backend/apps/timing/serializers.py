from rest_framework import serializers

from . import models


class TimingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TimingRecord
        fields = ['time', 'remark', 'type', 'start_time', 'end_time']

    type = serializers.CharField(source='get_type_display')
    start_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    end_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

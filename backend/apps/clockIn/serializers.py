from rest_framework.serializers import ModelSerializer
from ..clockIn.models import ClockIn


class ClockInSerializer(ModelSerializer):
    class Meta:
        model = ClockIn
        fields = "__all__"


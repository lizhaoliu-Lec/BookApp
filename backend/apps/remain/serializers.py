from rest_framework.serializers import ModelSerializer
from ..remain.models import Remain


class RemainSerializer(ModelSerializer):
    class Meta:
        model = Remain
        fields = "__all__"


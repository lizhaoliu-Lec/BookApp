from rest_framework.serializers import ModelSerializer
from ..statistic.models import Statistic


class StatisticSerializer(ModelSerializer):
    class Meta:
        model = Statistic
        fields = "__all__"
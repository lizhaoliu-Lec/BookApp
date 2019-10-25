from rest_framework.serializers import ModelSerializer
from ..todoSet.models import TodoSet


class TodoSetSerializer(ModelSerializer):
    class Meta:
        model = TodoSet
        fields = "__all__"


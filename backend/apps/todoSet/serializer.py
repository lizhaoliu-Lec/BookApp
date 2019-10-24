from rest_framework.serializers import ModelSerializer
from ..todoSet.models import TodoSet


class TodoSetSerializer(ModelSerializer):
    class Meta:
        models = TodoSet
        fields = "__all__"


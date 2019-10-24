from django.db import models
from ..todo.models import Todo


# Create your models here.
class Clock(models.Model):
    startTime = models.DateTimeField(auto_now=True)
    endTime = models.DateTimeField(auto_now=True)
    isCompleted = models.BooleanField()
    reason = models.CharField(max_length=255)
    belongTodo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name="belongTodo")

    class Meta:
        db_table = "Clock"



from django.db import models
from ..todo.models import Todo


# Create your models here.
class Clock(models.Model):
    startTime = models.DateTimeField(auto_now_add=True)
    endTime = models.DateTimeField(auto_now_add=True)
    isCompleted = models.BooleanField(default=0)
    reason = models.CharField(max_length=255)
    belongTodo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name="belongTodo")

    class Meta:
        db_table = "Clock"



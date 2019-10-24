from django.db import models
from ..todoSet.models import TodoSet


# Create your models here.
class Todo(models.Model):
    CLOCK_TYPE = (
        (0, '普通番茄钟'),
        (1, '养习惯'),
        (2, '定目标'),
    )

    LOOP_MODE = (
        (0, '每天'),
        (1, '每周'),
        (2, '每月')
    )

    name = models.CharField(max_length=50)
    attendTimes = models.PositiveIntegerField()
    quitTimes = models.PositiveIntegerField()
    totalTime = models.PositiveIntegerField()
    deadline = models.DateTimeField(auto_now=True)
    type = models.IntegerField(choices=CLOCK_TYPE)
    loopMode = models.IntegerField(choices=LOOP_MODE)
    expectedTime = models.PositiveIntegerField()
    belongTodoSet = models.ForeignKey(TodoSet, on_delete=models.CASCADE, related_name="belongTodoSet")

    class Meta:
        db_table = 'Todo'


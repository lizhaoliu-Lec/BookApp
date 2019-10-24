from django.db import models


# Create your models here.
class TodoSet(models.Model):
    name = models.CharField(max_length=50)
    todoNum = models.PositiveIntegerField()

    class Meta:
        db_table = 'TodoSet'



from django.db import models
from ..user.models import User


# Create your models here.
class TodoSet(models.Model):
    name = models.CharField(max_length=50, default="默认文件夹")
    todoNum = models.PositiveIntegerField(default=0, null=True)
    belongUser = models.ForeignKey(User, related_name="belongUser", on_delete=models.CASCADE)

    class Meta:
        db_table = 'TodoSet'




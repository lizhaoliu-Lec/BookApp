from django.db import models
from ..user.models import User


# Create your models here.
class Remain(models.Model):
    LOOP_MODE = (
        (0, '每天'),
        (1, '每周'),
        (2, '每月')
    )
    detail = models.CharField(max_length=255)
    timeToRemind = models.DateTimeField()
    repeatDay = models.IntegerField(choices=LOOP_MODE, null=True, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id")

    class Meta:
        db_table = 'Remain'



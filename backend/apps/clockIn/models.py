from django.db import models
from ..user.models import User


# Create your models here.
class ClockIn(models.Model):
    CLOCK_TYPE = (
        (0, '普通番茄钟'),
        (1, '养习惯'),
        (2, '定目标'),
    )

    punchTime = models.DateTimeField()
    type = models.IntegerField(choices=CLOCK_TYPE, null=True, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ClockIn'

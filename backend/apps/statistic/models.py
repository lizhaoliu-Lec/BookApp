from django.db import models
from ..user.models import User


# Create your models here.
class Statistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.PositiveIntegerField()
    month = models.PositiveIntegerField()

    class Meta:
        db_table = 'Statistic'




from django.db import models

from ..user.models import User


class TimingRecord(models.Model):
    class Meta:
        db_table = 'timing_record'

    TIMING_TYPE = (
        (0, '学习'),
        (1, '早起打卡'),
        (2, '睡觉打卡'),
    )

    record_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=None)
    time = models.IntegerField()
    remark = models.CharField(max_length=200)
    type = models.IntegerField(choices=TIMING_TYPE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)


class TimingGroup(models.Model):
    class Meta:
        db_table = 'timing_group'

    group_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    user = models.ManyToManyField(User, )


class TimingPlan(models.Model):
    class Meta:
        db_table = 'timing_plan'

    plan_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=None, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

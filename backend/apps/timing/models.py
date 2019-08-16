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

    user = models.ForeignKey(User, on_delete=None)
    time = models.IntegerField(null=True, blank=True)
    remark = models.CharField(max_length=200)
    type = models.IntegerField(choices=TIMING_TYPE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now=True)
    modified_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s-%s-%s' % (self.user, self.remark, self.time)


class TimingGroup(models.Model):
    class Meta:
        db_table = 'timing_group'

    description = models.CharField(max_length=200, null=True, blank=True)
    user = models.ManyToManyField(User)
    created_datetime = models.DateTimeField(auto_now=True)
    modified_datetime = models.DateTimeField(auto_now_add=True)


class TimingPlan(models.Model):
    class Meta:
        db_table = 'timing_plan'

    user = models.ForeignKey(User, on_delete=None, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now=True)
    modified_datetime = models.DateTimeField(auto_now_add=True)

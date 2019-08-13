import os
import random
import django

from django.utils import timezone as datetime
import pytz

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

django.setup()

from apps.user import models
from apps.timing import models


def insert():
    users = [
        {'account': '1234567', 'password': '1234567', 'name': '哈哈哈'},
        {'account': '098765', 'password': '098765', 'name': '嘻嘻嘻'},
        {'account': '147qwe', 'password': '147qwe', 'name': '猜猜我是谁'},
        {'account': '78654ghj', 'password': '78654ghj', 'name': '我不知道你是谁'},
        {'account': '99999999', 'password': '99999999', 'name': '好吧'},
        {'account': '6666666666', 'password': '6666666666', 'name': '自闭辽'},
    ]

    timing_records = [
        {'user': None, 'time': random.randint(1, 10), 'remark': '今天也要加油啊', 'type': 0,
         'start_time': datetime.datetime.now(),
         'end_time': datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 10))},
        {'user': None, 'time': random.randint(1, 10), 'remark': '今天要早起！', 'type': 1,
         'start_time': datetime.datetime.now(),
         'end_time': datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 10))},
        {'user': None, 'time': random.randint(1, 10), 'remark': '今天要早睡！', 'type': 2,
         'start_time': datetime.datetime.now(),
         'end_time': datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 10))},
        {'user': None, 'time': random.randint(1, 10), 'remark': '今天玩一天！', 'type': 0,
         'start_time': datetime.datetime.now(),
         'end_time': datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 10))},
        {'user': None, 'time': random.randint(1, 10), 'remark': '今天开心一下！', 'type': 0,
         'start_time': datetime.datetime.now(),
         'end_time': datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 10))},
        {'user': None, 'time': random.randint(1, 10), 'remark': '今天就皮革查吧。。。', 'type': 0,
         'start_time': datetime.datetime.now(),
         'end_time': datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 10))},
    ]

    timing_groups = [
        {'description': '这是一个开心的组啊！！！', 'group_id': 0},
        {'description': '这是一个哈哈哈哈的组啊！！！', 'group_id': 1},
        {'description': '这是一个无语无语与无语的组啊！！！', 'group_id': 2},
    ]

    timing_plans = [
        {'plan_id': 0, 'user': None, 'description': '今天我要跑是个实验！'},
        {'plan_id': 1, 'user': None, 'description': '早起是必须的！！'},
        {'plan_id': 2, 'user': None, 'description': '不早睡，等死吗？！'},
        {'plan_id': 3, 'user': None, 'description': '人生必须及时行乐！！'},
        {'plan_id': 4, 'user': None, 'description': '我岂止开心一下？？？'},
        {'plan_id': 5, 'user': None, 'description': '傻逼江南皮革厂。。。。。'},
    ]

    user_objs = []
    for user in users:
        user = models.User(**user)
        user.save()
        user_objs.append(user)

    for idx, timing_record in enumerate(timing_records):
        timing_record['user'] = user_objs[idx]
        timing_record = models.TimingRecord(**timing_record)
        timing_record.save()

    for idx, timing_group in enumerate(timing_groups):
        timing_group_obj = models.TimingGroup(**timing_group)
        timing_group_obj.save()
        timing_group_obj.user.add(*user_objs[2 * idx:2 + 2 * idx])

    for idx, timing_plan in enumerate(timing_plans):
        timing_plan['user'] = user_objs[idx]
        timing_plan = models.TimingPlan(**timing_plan)
        timing_plan.save()


if __name__ == '__main__':
    insert()

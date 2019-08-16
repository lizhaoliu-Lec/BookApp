import os
import random
import django

from django.utils import timezone as datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

django.setup()

from apps.user import models
from apps.timing import models


def insert():
    names = [
        '七喜先生',
        '全幼儿园最可爱',
        '诸多诱惑',
        '叼辣条闯世界',
        '李拔皮',
        '纯味野猫',
        '一懒众山小.',
        '孤独患者',
        '汤圆.',
        '拿着试卷唱忐忑',
        '同学，你狠屌？',
        '玩贴吧的好菇凉',
        '青春期躁动症',
        '本人已死, 有事烧纸',
        '吐舌奶包吴市长'
        '丑到未知丑',
        '我已长发及屁股',
    ]
    users = [
        {'account': '1234567', 'password': '1234567', 'name': names[random.randint(0, len(names) - 1)]},
        {'account': '098765', 'password': '098765', 'name': names[random.randint(0, len(names) - 1)]},
        {'account': '147qwe', 'password': '147qwe', 'name': names[random.randint(0, len(names) - 1)]},
        {'account': '78654ghj', 'password': '78654ghj', 'name': names[random.randint(0, len(names) - 1)]},
        {'account': '99999999', 'password': '99999999', 'name': names[random.randint(0, len(names) - 1)]},
        {'account': '6666666666', 'password': '6666666666', 'name': names[random.randint(0, len(names) - 1)]},
    ]

    remarks = [
        '人活着要有生活的目标：一辈子的目标，一段时间的目标，一个阶段的目标，一年的目标，'
        '一个月的目标，一个星期的目标，一天一小时一分钟的目标。——列夫·托尔斯泰',
        '管理的控制工作是务使实践活动符合于计划。——戈茨',
        '知识给人以份量，行为给人以光泽。——卡莱尔',
        '一个人的真正伟大之处就在于他能够认识到自己的渺小。——保罗',
        '人生至关重要的事是有远大的目标和达到这个目标的雄心壮志。——歌德',
        '做你所应做的事情，能有什么结果在其次。——赫伯脱',
        '想升高，有两样东西，那就是必须作鹰，或者作爬行动物。——巴尔扎克',
        '一个没有理想与目标的人，在思想上往往偏于保守；在行动上，常常想维持现状。——土光敏夫',
        '经常地、自觉保持平衡，实际上就是计划性。——列宁',
        '人类要控制自己，做到有计划地增长。——毛泽东',
        '先相信自己，然后别人才会相信你。——罗曼·罗兰',
        '为伟大的事业而牺牲的人，绝对不算失败者。——拜伦',
        '订目标，做计划，大量的行动。——陈安之',
        '确定了人生目标的人，比那些彷徨失措的人，起步时便已领先几十步。有目标的生活，'
        '远比彷徨的生活幸福。没有人生目标的人，人生本身就是乏味无聊的。——卡耐基',
        '要想做一个真正的英雄是没有选择余地的，往往是要么成功要么成仁。——希契科克',
        '智者不做不可能的事情。——马辛格',
        '要做事，但不要做事务的奴隶。——英国',
        '管理就是预测和计划、组织、指挥、协调以及控制。——亨利·法约尔',
        '生产不会计算，诸事都会白干。——佚名',
        '除非你亲自尝试一下，否则你永远不知道你能够做什么。——玛利雅',
        '计划的制定比计划本身更为重要。——戴尔·麦康基',
        '由于你不可能做到你所希望做到的一切，因此，你就应当做到你能够做到的一切。——泰伦底乌斯',
        '有必要做的事情，不如现在就做。——斯莫伦特',
        '经常地自觉保持平衡，实际上就是计划性。——列宁',
        '计划的目的，在肯定今后几年，如何安人？——曾仕强',
        '百年寿限不准有，百年计划不可无。——佚名',
        '天赐食于鸟，而不投食于巢。——霍兰顿',
        '一个人应当摈弃那些令人心颤的杂念，全神贯注地走自己脚下的人生之路。——斯蒂文森',
        '要是我们只限于梦想，那么谁来使生活成为美丽的呢？——高尔基',
        '用百折不回的毅力，有计划地克服所有的困难。——毛泽东',
        '只须希望而没有行动的人，只能靠做梦来收获所得。——佚名',
        '强烈的信仰会赢取坚强的人，然后又使他们更坚强。——华特·贝基霍',
        '我相信强烈的目标，这种可以使人完成任何事情的诚恳精神，这种自我忠实，是使人的心灵成就在业的最大因素。——弗烈德利克·B·罗宾森',
        '一个人正如一只时钟，是以他的行动来定其价值的。——潘尼',
        '至诚可以前知，预测未来才能做好计划。——曾仕强',
        '想得好是聪明，计划得好更聪明，做得好是最聪明又是最好。——拿破仑',
        '闲时无计划，忙时多费力。——佚名',
    ]
    groups_descriptions = [
        "只要千百万劳动者团结得像一个人一样，跟随本阶级的优秀人物前进，胜利也就有了保证。",
        "不管一个人多么有才能，但是集体常常比他更聪明和更有力。",
        "村子团结力量大，家庭团结幸福多。",
        "单个的人是软弱无力的，就像漂流的鲁滨孙一样，只有同别人在一起，他才能完成许多事业。",
        "凡是经过考验的朋友，就应该把他们紧紧地团结在你的周围。",
        "共同的事业，共同的斗争，可以使人们产生忍受一切的力量。",
        "纪律能美化集体。",
        "经营企业，是许多环节的共同运作，差一个念头，就决定整个失败。",
        "凝聚产生力量;团结诞生希望。",
        "人的巨大的力量就在这里——觉得自己是在友好的集体里面。",
        "人们在一起可以做出单独一个人所不能做出的事业.",
        "人心齐，泰山移。",
        "三个臭皮匠，顶个诸葛亮。",
        "谁若认为自己是圣人，是埋没了的天才，谁若与集体脱离，谁的命运就要悲哀。",
        "谁若与集体脱离，谁的命运就要悲哀。",
        "谁要是蔑视周围的人，谁就永远不会是伟大的人。",
        "天时不如地利，地利不如人和。",
        "团结就是力量。",
        "团结就有力量和智慧，没有诚意实行平等或平等不充分，就不可能有持久而真诚的团结。",
    ]
    plan_descriptions = [
        '凡事预则立，不预则废。——佚名',
        '管理的控制工作是务使实践活动符合于计划。——戈茨',
        '管理就是预测和计划、组织、指挥、协调以及控制。——亨利·法约尔',
        '计划的目的，在肯定今后几年，如何安人？——曾仕',
        '经常地、自觉保持平衡，实际上就是计划性。——列宁',
        '计划是要做的，可是灵活变通也是必要的。',
        '没有计划的人，在紧要关头就像热锅上的蚂蚁，无法面对当下的情形。',
        '计划是人生中很重要的一步，计划生活，计划成功，计划需要计划的一切。',
        '计划是每一个成功者都需要重视的问题。',
        '计划是能看见成果的。',
        '做事没计划，盲人骑害马。——佚名',
        '至诚可以前知，预测未来才能做好计划。——曾仕强',
        '用百折不回的毅力，有计划地克服所有的困难。——毛泽东',
        '已经完成的小事，胜于计划中的大事。——雷特',
        '要做事，但不要做事务的奴隶。——英国',
        '闲时无计划，忙时多费力。——佚名',
        '算算用用，一世不穷；不算光用，海干山空。',
        '生产不会计算，诸事都会白干。——佚名',
        '人类要控制自己，做到有计划地增长。——毛泽东',
        '百年寿限不准有，百年计划不可无。——佚名',
        '长计划，短安排。——佚名',
        '吃不穷，穿不穷，打算不到就受穷。——佚名',
        '大计划要慎重考虑。——英国',
        '订目标，做计划，大量的行动。——陈安之',
        '凡谋之道，周密为宝。——《六韬》',
    ]

    INSERT_TIMES = 10

    for _ in range(INSERT_TIMES):
        timing_records = [
            {'user': None, 'time': random.randint(1, 10), 'remark': remarks[random.randint(0, len(remarks) - 1)],
             'type': random.randint(0, 2),
             'start_time': datetime.datetime.now(),
             'end_time': datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 10))},
            {'user': None, 'time': random.randint(1, 10), 'remark': remarks[random.randint(0, len(remarks) - 1)],
             'type': random.randint(0, 2),
             'start_time': datetime.datetime.now(),
             'end_time': datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 10))},
            {'user': None, 'time': random.randint(1, 10), 'remark': remarks[random.randint(0, len(remarks) - 1)],
             'type': random.randint(0, 2),
             'start_time': datetime.datetime.now(),
             'end_time': datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 10))},
            {'user': None, 'time': random.randint(1, 10), 'remark': remarks[random.randint(0, len(remarks) - 1)],
             'type': random.randint(0, 2),
             'start_time': datetime.datetime.now(),
             'end_time': datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 10))},
            {'user': None, 'time': random.randint(1, 10), 'remark': remarks[random.randint(0, len(remarks) - 1)],
             'type': random.randint(0, 2),
             'start_time': datetime.datetime.now(),
             'end_time': datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 10))},
            {'user': None, 'time': random.randint(1, 10), 'remark': remarks[random.randint(0, len(remarks) - 1)],
             'type': random.randint(0, 2),
             'start_time': datetime.datetime.now(),
             'end_time': datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 10))},
        ]

        timing_groups = [
            {'description': groups_descriptions[random.randint(0, len(groups_descriptions) - 1)]},
            {'description': groups_descriptions[random.randint(0, len(groups_descriptions) - 1)]},
            {'description': groups_descriptions[random.randint(0, len(groups_descriptions) - 1)]},
        ]

        timing_plans = [
            {'user': None, 'description': plan_descriptions[random.randint(0, len(plan_descriptions) - 1)]},
            {'user': None, 'description': plan_descriptions[random.randint(0, len(plan_descriptions) - 1)]},
            {'user': None, 'description': plan_descriptions[random.randint(0, len(plan_descriptions) - 1)]},
            {'user': None, 'description': plan_descriptions[random.randint(0, len(plan_descriptions) - 1)]},
            {'user': None, 'description': plan_descriptions[random.randint(0, len(plan_descriptions) - 1)]},
            {'user': None, 'description': plan_descriptions[random.randint(0, len(plan_descriptions) - 1)]},
        ]

        user_objs = []
        for user in users:
            user = models.User(**user)
            user.save()
            user_objs.append(user)

        random.shuffle(user_objs)
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

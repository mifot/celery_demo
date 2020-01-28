# from datetime import datetime, timedelta
# import tasks
#
#
# def reverse(name):
#     tasks.reverse.delay(name)
#     return 'done\n'
#
#
# def add(a):
#     a2 = a + 2
#     time = datetime.utcnow() + timedelta(seconds=30)
#     tasks.add.apply_async((2, int(a)), eta=time)
#     return a2
#
#
# version 2

from config import celery
from datetime import datetime, timedelta
# import tasks


def reverse(name):
    reversed.delay(name)
    return 'done\n'


def add(a):
    a2 = int(a) + 2
    time = datetime.utcnow() + timedelta(seconds=30)
    addd.apply_async((2, int(a)), eta=time)
    return a2


@celery.task
def addd(x, y):
    return x + y


@celery.task
def reversed(string):
    return string[::-1]



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
    reverse.delay(name)
    return 'done\n'


def add(a):
    a2 = a + 2
    time = datetime.utcnow() + timedelta(seconds=30)
    add.apply_async((2, int(a)), eta=time)
    return a2


@celery.task
def add(x, y):
    return x + y


@celery.task
def reverse(string):
    return string[::-1]



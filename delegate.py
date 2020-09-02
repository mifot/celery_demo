
from config import celery
from datetime import datetime, timedelta


def reverse(name):
    reverse_task.delay(name)
    return 'done\n'


def add(a):
    result = int(a) + 2
    time = datetime.utcnow() + timedelta(seconds=30)
    add_task.apply_async((2, int(a)), eta=time)
    return result


@celery.task
def times_task(x, y):
    return x * y


def times(a):
    result = int(a) * 2
    time = datetime.utcnow() - timedelta(seconds=1000)
    times_task.apply_async((2, int(a)), eta=time)
    return result


@celery.task
def add_task(x, y):
    return x + y


@celery.task
def reverse_task(string):
    time = datetime.utcnow() + timedelta(seconds=15)
    times_task.apply_async((2, 1), eta=time)
    return string[::-1]



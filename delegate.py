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

# from config import celery
from datetime import datetime, timedelta
# import tasks

# ------
# to do test docker-compose

from celery import Celery

CELERY_BROKER_URL = 'amqp://rabbitmq:rabbitmq@rabbit:5672/'
# CELERY_RESULT_BACKEND = 'rpc://'
# Initialize Celery
celery = Celery('worker', broker=CELERY_BROKER_URL)

# ------


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
    return string[::-1]



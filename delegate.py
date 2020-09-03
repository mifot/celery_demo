
from config import celery
from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.INFO)


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
    result = x * y
    logging.info("RESULT: {}".format(result))
    return


def times(a):
    result = int(a) * 2
    time = datetime.utcnow() - timedelta(seconds=1000)
    times_task.apply_async((2, int(a)), eta=time)
    return


@celery.task
def add_task(x, y):
    result = x + y
    logging.info("RESULT: {}".format(result))
    return


@celery.task
def reverse_task(string):

    time = datetime.utcnow() + timedelta(seconds=15)
    times_task.apply_async((2, 1), eta=time)

    result = string[::-1]
    logging.info("RESULT: {}".format(result))
    return

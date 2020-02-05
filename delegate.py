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
from task import times_task, add_task, reverse_task

# ------
# to do test docker-compose

# ------


def reverse(name):
    reverse_task.delay(name)
    return 'done\n'

def add(a):
    result = int(a) + 2
    time = datetime.utcnow() + timedelta(seconds=30)
    add_task.apply_async((2, int(a)), eta=time)
    return result


def times(a):
    result = int(a) * 2
    time = datetime.utcnow() - timedelta(seconds=1000)
    times_task.apply_async((2, int(a)), eta=time)
    return result





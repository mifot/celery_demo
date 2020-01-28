from datetime import datetime, timedelta
# from tasks import *
import tasks


def reverse(name):
    tasks.reverse.delay(name)
    return 'done'


def add(a):
    time = datetime.utcnow() + timedelta(seconds=30)
    tasks.add.apply_async((2, int(a)), eta=time)
    return 'done'



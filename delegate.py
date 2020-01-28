from datetime import datetime, timedelta
from tasks import *


def reverse(name):
    reverse.delay(name)
    return 'done'


def add(a):
    time = datetime.utcnow() + timedelta(seconds=30)
    add.apply_async((2, int(a)), eta=time)
    return 'done'

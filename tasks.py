from config import celery


@celery.task(name='delegate.add')
def add(x, y):
    return x + y


@celery.task(name='delegate.reverse')
def reverse(string):
    return string[::-1]

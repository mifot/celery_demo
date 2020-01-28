from config import celery


@celery.task
def add(x, y):
    return x + y


@celery.task
def reverse(string):
    return string[::-1]

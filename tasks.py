from config import celery


@celery.task#(name='server.add')
def add(x, y):
    return x + y


@celery.task#(name='server.reverse')
def reverse(string):
    return string[::-1]

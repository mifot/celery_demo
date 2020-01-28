from config import celery


@celery.task#(name='app.add')
def add(x, y):
    return x + y


@celery.task#(name='app.reverse')
def reverse(string):
    return string[::-1]

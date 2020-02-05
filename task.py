from celery import Celery

CELERY_BROKER_URL = 'amqp://rabbitmq:rabbitmq@rabbit:5672/'
# CELERY_RESULT_BACKEND = 'rpc://'
# Initialize Celery
celery = Celery('worker', broker=CELERY_BROKER_URL)#, backend=CELERY_RESULT_BACKEND)


@celery.task
def times_task(x, y):
    return x * y


@celery.task
def add_task(x, y):
    return x + y


@celery.task
def reverse_task(string):
    return string[::-1]
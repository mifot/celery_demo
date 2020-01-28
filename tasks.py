from celery import Celery
import time

# celery config
app = Celery('tasks', broker='amqp://localhost//')

# add tasks
@app.task
def reverse(string):
    time.sleep(15)
    return string[::-1]

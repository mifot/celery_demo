from celery import Celery

# celery config
app = Celery('tasks', broker='amqp://localhost//')

# add tasks
@app.task
def reverse(string):
    return string[::-1]

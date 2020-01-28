from flask import Flask
from flask_celery import make_celery
from datetime import datetime, timedelta

app = Flask(__name__)

app.config['CELERY_RESULT_BACKEND'] = 'amqp://localhost//'

celery = make_celery(app)


@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    return 'done'


@app.route('/add/<a>')
def add(a):
    time = datetime.utcnow() + timedelta(seconds=30)
    add.apply_async((2, a), eta=time)
    return 'done'


@celery.task
def add(x, y):
    return x + y


@celery.task(name='app.reverse')
def reverse(string):
    return string[::-1]


if __name__ == '__main__':
    app.run(debug=True)

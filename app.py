from flask import Flask
from flask_celery import make_celery

app = Flask(__name__)

app.config['CELERY_RESULT_BACKEND'] = 'amqp://localhost//'

celery = make_celery(app)


@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    return 'done'


@celery.task(name='app.reverse')
def reverse(string):
    return string[::-1]


if __name__ == '__main__':
    app.run(debug=True)

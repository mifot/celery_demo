from flask import Flask
from celery import Celery


def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://rabbitmq:rabbitmq@rabbit:5672/'
celery = make_celery(app)
app.config.task_default_queue = 'celery'


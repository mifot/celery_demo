from flask import Flask
from celery import Celery


def make_celery(app):
    celery = Celery(
        app.import_name,
        # backend=app.config['CELERY_RESULT_BACKEND'],
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
# app.config['CELERY_RESULT_BACKEND'] = 'amqp://localhost//'
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
celery = make_celery(app)


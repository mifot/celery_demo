# Celery demo with rabbitMQ (Redis can be used as well)
followed by https://www.youtube.com/playlist?list=PLXmMXHVSvS-DvYrjHcZOg7262I9sGBLFR

## instructions & tips

need to install rabbitmq server run:
> $ sudo apt-get install rabbitmq-server

sometimes rabbitmq have to be restarted before first use
> $ sudo service rabbitmq-server restart

to check status of rabbitMQ run:
> $ sudo rabbitmqctl status

before start program celery have to be started
> $ celery -A {filename_with_config} worker --loglevel=info


## notes
.delay() - add to queue
.apply_async((2, int(a)), eta=time) - in given time in eta format

celery just take a function and run it

the results of celery task can be stored in database [sqlite etc.] or Redis (add backend in config)

## links
https://celery.readthedocs.io/en/latest/getting-started/first-steps-with-celery.html  
https://flask.palletsprojects.com/en/1.1.x/patterns/celery/  
https://vinta.ws/code/run-a-celery-task-at-a-specific-time.html  
https://celery.readthedocs.io/en/latest/getting-started/first-steps-with-celery.html  
http://docs.celeryproject.org/en/master/userguide/calling.html#eta-and-countdown  
https://hub.docker.com/_/celery
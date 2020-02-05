#!/bin/bash

pipenv run celery -A task.celery worker --autoscale=5,2 --loglevel=info
FROM python:3.6
EXPOSE 8080
RUN apt-get update && apt-get install -y python3-dev
RUN ["pip3", "install", "pipenv"]
#
WORKDIR /app

# copy only pipfiles to install dependencies
COPY . .
RUN ["pipenv", "install"]
#ENV LC_ALL=C.UTF-8
#ENV LANG=C.UTF-8


#RUN pipenv lock --requirements > requirements.txt
#RUN pip3 install -r requirements.txt

# setup env variables to initialize database
#
#ENV RABBITMQ_URL='amqp://rabbitmq:rabbitmq@rabbit:5672/'
#ENV DATABASE_URL=

ENV FLASK_APP=server.py
#
#RUN ["pipenv", "run", "flask", "db", "upgrade"]
#
CMD ["pipenv", "run", "python", "server.py"]
#CMD python3 server.py
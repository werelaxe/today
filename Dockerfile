FROM ubuntu:16.04

LABEL maintainer="werelaxe"

RUN apt-get update && apt-get install python3 curl -y
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python3 get-pip.py
RUN pip3 install Django
RUN pip3 install djangorestframework
RUN pip3 install requests

RUN mkdir app
WORKDIR app

COPY . /app
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:80"]

FROM python:3.9-buster

RUN apt update && apt upgrade -y && apt install python3-dev python3-pip -y

COPY . /app

WORKDIR /app

EXPOSE 8000

RUN pip3 install --upgrade -r /app/requirements.txt

CMD python3 manage.py runserver 0.0.0.0:8000
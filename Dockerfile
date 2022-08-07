FROM python:3.8-slim-buster

RUN apt-get update

WORKDIR /myapp

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn","-w","4","-t","600","wsgi:app","--bind", "0.0.0.0:5000"]
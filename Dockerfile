FROM python:3.7
FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD=DB_PASSWORD

MAINTAINER Dike <dike.dim@protonmail.com>

WORKDIR /flask_portfolio

COPY ./requirements.txt /flask_porfolio

RUN python -m venv venv

RUN venv/bin/pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "run", "--port=5000"]
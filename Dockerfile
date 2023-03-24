ARG PYVER=3.11
FROM debian:sid-20230202
ARG PYVER

MAINTAINER Dike <dike.dim@protonmail.com>

WORKDIR /flask_portfolio

COPY ./requirements.txt /flask_porfolio

RUN apt update

RUN apt install -y python${PYVER}-venv

RUN python3 -m venv venv

COPY . .
 
RUN bash -c 'source venv/bin/activate && pip install --no-cache-dir -r requirements.txt'

EXPOSE 5000

ENV MYSQL_ROOT_PASSWORD=${DB_PASSWORD}
ENV PYTHONPATH /flask_portfolio/venv/lib/python${PYVER}/site-packages
CMD ["bash", "-cx", "source venv/bin/activate && python3 -m flask run --host=0.0.0.0 --port=5000"]

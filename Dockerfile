FROM python

ENV PYTHONUNBUFFERED 1

WORKDIR /app1

ADD . /app1

COPY ./requirements.txt /fit/requirements.txt

RUN pip install -r requirements.txt

COPY . /app1

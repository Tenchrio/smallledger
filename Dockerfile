FROM python:3.7
MAINTAINER tenchrio
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
RUN python manage.py migrate
CMD exec gunicorn SmallLedger.wsgi:application --bind 0.0.0.0:8000

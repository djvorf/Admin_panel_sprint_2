FROM python:3.9
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /movie_admin
COPY requirements /movie_admin/requirements
RUN pip install -r requirements/production.txt
COPY . /movie_admin/
CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000
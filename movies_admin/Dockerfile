FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /movie_admin
COPY . /movie_admin/
RUN pip install -r requirements/base.txt
RUN pip install -r requirements/production.txt
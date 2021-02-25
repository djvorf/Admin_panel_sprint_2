FROM python:3.9
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV SECRET_KEY=csdmklcmklLK#MKMFCLKMDLKvmklsmdlkvmvlmdslkvsmdvl
ENV SECRET_KEY=csdmklcmklLK#MKMFCLKMDLKvmklsmdlkvmvlmdslkvsmdvl
ENV DBNAME=postgres
ENV DBUSER=postgres
ENV DBPASSWORD=postgres
ENV DBHOST=postgres
ENV DBPORT=5432
WORKDIR /movie_admin
COPY requirements /movie_admin/requirements
RUN pip install -r requirements/production.txt
COPY . /movie_admin/
CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000
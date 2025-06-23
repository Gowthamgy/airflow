# Dockerfile
FROM apache/airflow:2.9.2-python3.10

USER root
RUN apt-get update && apt-get install -y gcc libmysqlclient-dev

USER airflow
COPY ./scraper /opt/airflow/scraper

RUN pip install scrapy mysql-connector-python mysqlclient
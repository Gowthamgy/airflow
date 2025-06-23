from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='run_scrapy_spider',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    run_spider = BashOperator(
        task_id='run_sample_spider',
        bash_command='cd /opt/airflow/scraper && scrapy crawl sample',
    )

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def ingest_data():
    # Your earlier pandas read_csv logic here
    pass

def process_data():
    # Your cleaning/enriching code here
    pass

def aggregate_data():
    # Your aggregation logic here
    pass

def load_to_db():
    # Your database write logic here
    pass

with DAG('ecommerce_etl',
        start_date=datetime(2025, 10, 1),
        schedule_interval='@daily',
        catchup=False) as dag:
    ingest = PythonOperator(task_id='ingest_data', python_callable=ingest_data)
    process = PythonOperator(task_id='process_data', python_callable=process_data)
    aggregate = PythonOperator(task_id='aggregate_data', python_callable=aggregate_data)
    load = PythonOperator(task_id='load_to_db', python_callable=load_to_db)

    ingest >> process >> aggregate >> load

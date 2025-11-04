from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from data_ingestion.download_seviri import query_and_download_seviri
from data_processing.transform_xarray import process_seviri
from database.db_loader import load_to_database

default_args = {
    'owner': 'berkesenturk',
    'depends_on_past': False,
    'email_on_failure': True,
    'email': ['berkesenturk11@gmail.com'],
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'etl_seviri_dag',
    default_args=default_args,
    description='Batch ETL pipeline for Meteosat SEVIRI imagery',
    schedule_interval='@daily',
    start_date=datetime(2025, 10, 1),
    catchup=False
)

download_task = PythonOperator(
    task_id='download_seviri_data',
    python_callable=query_and_download_seviri,
    dag=dag
)

process_task = PythonOperator(
    task_id='process_seviri_data',
    python_callable=process_seviri,
    dag=dag
)

store_task = PythonOperator(
    task_id='store_metrics_db',
    python_callable=load_to_database,
    dag=dag
)

download_task >> process_task >> store_task
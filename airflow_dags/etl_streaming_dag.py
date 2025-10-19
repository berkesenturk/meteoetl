from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from streaming.kafka_producer import produce_stream

default_args = {
    'owner': 'berkesenturk',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

dag = DAG(
    'etl_streaming_dag',
    default_args=default_args,
    description='Streaming Kafka producer DAG for SEVIRI',
    schedule_interval='@hourly',
    start_date=datetime(2025, 10, 1),
    catchup=False
)

produce = PythonOperator(
    task_id='produce_kafka_events',
    python_callable=produce_stream,
    dag=dag
)
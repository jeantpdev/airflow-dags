from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta

# Define los argumentos por defecto del DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instancia el objeto DAG
dag = DAG(
    'mi_primer_dag',
    default_args=default_args,
    description='Un simple DAG de ejemplo',
    schedule_interval=timedelta(days=1)  # Ejecutar una vez al día
)

inicio = DummyOperator(task_id='inicio', dag=dag)
tarea_final = DummyOperator(task_id='tarea_final', dag=dag)

inicio >> tarea_final

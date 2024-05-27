from airflow import DAG
from airflow.operators.bash_operator import BashOperator
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
    'mi_dag_simple',
    default_args=default_args,
    description='Un simple DAG de ETL',
    schedule_interval=timedelta(days=1)  # Ejecutar una vez al día
)

# Tarea de Extracción
extraccion = BashOperator(
    task_id='extraccion',
    bash_command='echo "Extrayendo datos..."',
    dag=dag
)

# Tarea de Transformación
transformacion = BashOperator(
    task_id='transformacion',
    bash_command='echo "Transformando datos..."',
    dag=dag
)

# Tarea de Carga
carga = BashOperator(
    task_id='carga',
    bash_command='echo "Cargando datos..."',
    dag=dag
)

# Definir el flujo de tareas
extraccion >> transformacion >> carga

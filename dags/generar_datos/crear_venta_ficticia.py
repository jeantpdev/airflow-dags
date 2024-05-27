from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from generar_datos.utils import utilidades
import requests

def generar_datos_cliente():
    datos_cliente = {
        'nombre': utilidades.generar_nombre_aleatorio(),
        'dni': utilidades.generar_dni_aleatorio(),
        'telefono': utilidades.generar_telefono_aleatorio(),
        'telefono_fijo': utilidades.generar_telefono_aleatorio(),
        'correo': utilidades.generar_correo_aleatorio(),
        'direccion': utilidades.generar_direccion_aleatoria(),
        'fecha_nacimiento': utilidades.generar_fecha_nacimiento().strftime('%Y-%m-%d'),
        'cups_luz': utilidades.cups_luz_aleatorio(),
        'cups_gas': utilidades.cups_gas_aleatorio(),
        'iban': utilidades.generar_iban_aleatorio(),
        'numero_contrato': utilidades.generar_contrato_aleatorio(),
        'potencia': utilidades.generar_potencia_aleatorio(),
        'peaje_gas': utilidades.generar_peaje_gas_aleatorio(),
        'mantenimiento': utilidades.generar_mantenimiento_aleatorio(),
        'tipo_mantenimiento': utilidades.generar_tipo_mantenimiento_aleatorio(),
        'compania': utilidades.generar_compania_aleatorio()
    }
    print(datos_cliente)
    return datos_cliente

def generar_datos_calidad():
    datos_calidad = {
        'llamada_realizada': bool(False),
        'calidad_enviada': bool(False),
        'observaciones_calidad': "por revisar",
        'audios_cargados': bool(False),
        'verificacion': bool(False)
    }
    print(datos_calidad)
    return datos_calidad

def generar_datos_agente():
    agente = {
        'cedula': utilidades.cedula_aleatoria(),
        'fecha_ingreso': utilidades.generar_fecha_hoy().strftime('%Y-%m-%d'),
        'observaciones_venta': utilidades.cedula_aleatoria(),
        'estado': utilidades.estados_aleatorio()
    }
    print(agente)
    return agente

def preparar_datos(ti):
    datos_cliente = generar_datos_cliente()
    datos_calidad = generar_datos_calidad()
    agente = generar_datos_agente()
    ti.xcom_push(key='datos_cliente', value=datos_cliente)
    ti.xcom_push(key='datos_calidad', value=datos_calidad)
    ti.xcom_push(key='agente', value=agente)

def insertar_data_bd(ti):
    datos_cliente = ti.xcom_pull(key='datos_cliente', task_ids='generar_datos_task')
    datos_calidad = ti.xcom_pull(key='datos_calidad', task_ids='generar_datos_task')
    agente = ti.xcom_pull(key='agente', task_ids='generar_datos_task')
    datos = {**datos_cliente, **datos_calidad, **agente}
    api_url = 'http://host.docker.internal:5700/crear-venta/'
    response = requests.post(api_url, json=datos)
    print(response)

# Define los argumentos por defecto del DAG
default_args = {
    'owner': 'Jean Trujillo',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 27),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instancia el objeto DAG
dag = DAG(
    'generar_venta_ficticia',
    default_args=default_args,
    description='Un simple DAG para generar ventas ficticias',
    schedule_interval=timedelta(minutes=2)
)

# Crear una tarea utilizando el operador PythonOperator para preparar_datos
generar_datos_task = PythonOperator(
    task_id='generar_datos_task',
    python_callable=preparar_datos,
    provide_context=True,
    dag=dag
)

# Crear una tarea utilizando el operador PythonOperator para insertar_data_bd
crear_datos_task = PythonOperator(
    task_id='cargar_datos_bd_task',
    python_callable=insertar_data_bd,
    provide_context=True,
    dag=dag
)

# Definir el flujo de tareas
generar_datos_task >> crear_datos_task

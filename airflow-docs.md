# Airflow

##### **¿Qué es Airflow?**
Apache Airflow es una plataforma de gestión de flujos de trabajo y orquestación de datos. Se utiliza principalmente para programar y monitorear flujos de trabajo complejos. Airflow permite definir, programar y monitorizar flujos de trabajo de manera programática utilizando Python, lo que facilita la automatización de tareas repetitivas y la integración de múltiples sistemas de datos.

##### Detalles del Flujo de Trabajo

1. **Inicio del DAG**: Airflow Scheduler comprueba los DAGs programados y decide cuándo ejecutar cada DAG basado en su `schedule_interval`.
2. **Ejecución de Tareas**: Las tareas se ejecutan en el orden definido por sus dependencias. Cada tarea se puede ejecutar en un worker diferente.
3. **Monitoreo en Tiempo Real**: A través de la interfaz web de Airflow, puedes monitorear la ejecución de cada tarea, ver logs y tomar acciones si es necesario.
4. **Reintentos y Fallos**: Si una tarea falla, se reintenta según los parámetros definidos (`retries` y `retry_delay`). Si sigue fallando, se marca como fallida y puede desencadenar alertas.
5. **Finalización**: Una vez que todas las tareas del DAG se completan, el DAG se considera completado para esa instancia programada.

## Crear un DAG

#### Importar las librerías necesarias:
```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
```

#### Función que se ejecutará:
```python
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
```
Una simple función que retorna un diccionario.

#### Argumentos del DAG
```python
default_args = {
    'owner': 'Jean Trujillo',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 27),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
```
Son los detalles del DAG a crear. Contiene información necesaria en caso de que falle un proceso o enviar un correo si llega a fallar.

* retries: Numero de intentos por si llega a fallar
* retry_delay: Si llega a ocurrir un error, volverá a ejecutarse dentro del tiempo que se le establezca

#### Instancia de un DAG
```python
dag = DAG(
    'generar_venta_ficticia', #nombre del dag
    default_args=default_args,
    description='Un simple DAG para generar ventas ficticias',
    schedule_interval=timedelta(minutes=2)
)
```
Configuración del DAG. Contiene el nombre del DAG, su descripción y cada cuanto se va a ejecutar.
* schedule_interval: Cada cuanto se va a ejecutar el DAG.

#### Creación de una tarea de Python
```python
task_name = PythonOperator(
    task_id='nombre_tarea',
    python_callable=preparar_datos,
    provide_context=True,
    dag=dag
)
```
Al ser de python, se usa el operador PythonOperator y este nos pide información como:
* task_id: ID con el que identificaremos el task.
* python_callable: La función que va a ejecutar la tarea.

#### Flujo de tareas:
```python
nombre_tarea >> nombre_tarea2
```
Se detalla el orden en el que tiene que ejecutarse las tareas; va al final del archivo
## Parámetros entre funciones

Para retornar resultados de funciones a otras funciones, hay que usar
```python
ti.xcom_push(key='nombre_retorno', value=valor_retorno)
```

Ejemplo:
```python
def preparar_datos(ti):
    datos_cliente = generar_datos_cliente()
    datos_calidad = generar_datos_calidad()
    agente = generar_datos_agente()

    ti.xcom_push(key='datos_cliente', value=datos_cliente)
    ti.xcom_push(key='datos_calidad', value=datos_calidad)
    ti.xcom_push(key='agente', value=agente)
```

Para recibir el parametro hay que tener en cuenta el id de la tarea (task-ids) y el "key" con el que lo retornamos:
```python
def insertar_data_bd(ti):
    datos_cliente = ti.xcom_pull(key='nombre_retorno', task_ids='nombre_tarea')
```

Ejemplo:
```python
def insertar_data_bd(ti):

    datos_cliente = ti.xcom_pull(key='datos_cliente', task_ids='generar_datos_task')

    datos_calidad = ti.xcom_pull(key='datos_calidad', task_ids='generar_datos_task')

    agente = ti.xcom_pull(key='agente', task_ids='generar_datos_task')
```

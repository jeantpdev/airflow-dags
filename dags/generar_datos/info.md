# Creacion de ventas ficticias

### Descripcion:

DAG que crea ventas ficticias con los siguientes datos:

```json
{
    datos_cliente:
        nombre
        dni
        telefono
        telefono_fijo
        correo
        direccion
        fecha_nacimiento
        cups_luz
        cups_gas
        iban
        numero_contrato
        potencia
        peaje_gas
        mantenimiento
        tipo_mantenimiento
        compania
}
```

```json
{   
    datos_calidad:
        llamada_realizada
        calidad_enviada
        observaciones_calidad
        audios_cargados
        verificacion
}
```

```json
{   
    agente:
        cedula
        fecha_ingreso
        observaciones_venta
        estado
}
```

### Objetivo:

Llenar una base de datos con información de ventas para poder practicar consultas en SQL y crear informes con Power BI.

### Información del Dag:

#### Tareas
**Tarea generar_datos_task:**
**task_id** = 'generar_datos_task'
**funcion** = preparar_datos

**Tarea cargar_datos_bd_task:**
**task_id** = 'cargar_datos_bd_task'
**funcion** = insertar_data_bd

#### Flujo de tareas
generar_datos_task >> crear_datos_task
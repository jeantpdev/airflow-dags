import random
from datetime import datetime, timedelta
import string

class utilidades:

# Listas de nombres y apellidos comunes

    def generar_direccion_aleatoria():

        nombres_calle = ['Calle Falsa', 'Avenida Siempreviva', 'Boulevard del Sol', 'Paseo de la Reforma', 'Calle de la Luna']
        tipos_via = ['Calle', 'Avenida', 'Boulevard', 'Paseo', 'Camino']
        ciudades = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Zaragoza']
        provincias = ['Madrid', 'Cataluña', 'Comunidad Valenciana', 'Andalucía', 'Aragón']
        codigos_postales = ['28001', '08001', '46001', '41001', '50001']
        nombre_calle = random.choice(nombres_calle)
        tipo_via = random.choice(tipos_via)
        numero = random.randint(1, 100)
        ciudad = random.choice(ciudades)
        provincia = random.choice(provincias)
        codigo_postal = random.choice(codigos_postales)
        
        direccion = f'{tipo_via} {nombre_calle} {numero}, {codigo_postal} {ciudad}, {provincia}'
        return direccion

    def generar_nombre_aleatorio():
        nombres = ['Juan', 'María', 'José', 'Ana', 'Pedro', 'Luis', 'Marta', 'Carlos', 'Laura', 'David']
        apellidos = ['García', 'Martínez', 'López', 'González', 'Rodríguez', 'Fernández', 'Pérez', 'Martín', 'Sánchez', 'Jiménez']

        # Seleccionar un nombre aleatorio de la lista de nombres y un apellido aleatorio de la lista de apellidos
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        # Retornar el nombre completo
        return f"{nombre} {apellido}"
    
    def cedula_aleatoria():
        cedulas = ["1234569", "00300800", "122333", "12233344", "44332211"]
        cedula_elegida = random.choice(cedulas)
        return cedula_elegida

    def estados_aleatorio():
        estados = ["activa", "cancelada", "devuelta", "tramite alta", "temporal"]
        estado_elegido = random.choice(estados)
        return estado_elegido
    
    def cups_luz_aleatorio():
        cups_luz_elegido = random.randint(1000, 10000)
        return f'E{cups_luz_elegido}'
    
    def cups_gas_aleatorio():
        cups_gas_elegido = random.randint(1000, 10000)
        return f'E{cups_gas_elegido}'
    
    def generar_usuario_aleatorio():
        caracteres = string.ascii_letters + string.digits
        longitud = random.randint(5, 10)  # Longitud aleatoria para el nombre de usuario
        return ''.join(random.choice(caracteres) for _ in range(longitud))

    # Función para generar un dominio de correo electrónico aleatorio
    def generar_dominio_aleatorio():
        dominios = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com']
        return random.choice(dominios)

    # Generar una dirección de correo electrónico aleatoria
    def generar_correo_aleatorio():
        usuario = utilidades.generar_usuario_aleatorio()
        dominio = utilidades.generar_dominio_aleatorio()
        return f"{usuario}@{dominio}"
    
    def generar_dni_aleatorio():
        iban_elegido = random.randint(4000, 10000)
        letras = ["E", "X", "B", "F", "N"]
        return f'{random.choice(letras)}{iban_elegido}'
    
    def generar_iban_aleatorio():
        iban_elegido = random.randint(1000, 10000)
        return f'E{iban_elegido}'
    
    def generar_contrato_aleatorio():
        contrato_elegido = random.randint(1000, 10000)
        return f'{contrato_elegido}'
    
    def generar_potencia_aleatorio():
        potencia_elegido = random.randint(1, 50)
        return f'{potencia_elegido}kw'
    
    def generar_peaje_gas_aleatorio():
        peaje_gas_elegido = random.randint(1000, 10000)
        return f'{peaje_gas_elegido}'
    
    def generar_mantenimiento_aleatorio():
        mantenimientos = ["Pack235", "Pack todo", "20 Descuento", "Brilla", "Bienvenida"]
        mantenimiento_elegida = random.choice(mantenimientos)
        return mantenimiento_elegida
    
    def generar_tipo_mantenimiento_aleatorio():
        mantenimientos = ["CCV", "KK", "EE", "VV", "CC", "DDF", "BBD"]
        mantenimiento_elegida = random.choice(mantenimientos)
        return mantenimiento_elegida
    
    def generar_telefono_aleatorio():
        telefono_elegida = random.randint(1000, 10000)
        return telefono_elegida
    
    def generar_compania_aleatorio():
        mantenimientos = ["iberdrola", "naturgy"]
        mantenimiento_elegida = random.choice(mantenimientos)
        return mantenimiento_elegida
    
    def observaciones_aleatorias():
        observaciones_posibles = [
            "Cliente muy interesado en el producto",
            "Cliente necesita tiempo para pensar",
            "Cliente no está seguro sobre el precio",
            "Cliente tiene objeciones sobre las características del producto",
            "Cliente muestra interés en una futura compra",
            "Cliente solicita más información",
            "Venta cerrada con éxito",
            "Cliente se retiró sin comprar",
            "Cliente expresó insatisfacción con el producto",
            "Cliente está considerando otras opciones",
            "Cliente necesita consultar con alguien más antes de decidir",
            "Cliente no está listo para comprar en este momento"
        ]
        observaciones_venta = random.choice(observaciones_posibles)
        return observaciones_venta


    # Generar fechas aleatorias dentro del rango especificado
    def generar_fecha_aleatoria():
        fecha_inicio = datetime(2023, 6, 1)
        fecha_fin = datetime(2024, 6, 30)
        # Generar un número aleatorio de días desde la fecha de inicio hasta la fecha de fin
        dias_aleatorios = random.randint(0, (fecha_fin - fecha_inicio).days)
        # Sumar ese número de días a la fecha de inicio para obtener una fecha aleatoria dentro del rango
        fecha_aleatoria = fecha_inicio + timedelta(days=dias_aleatorios)
        return fecha_aleatoria
    
    def generar_fecha_hoy():
        # Obtiene la fecha y hora actuales
        fecha_hoy = datetime.now()
        # Devuelve la fecha y hora actuales
        return fecha_hoy
    
    def generar_fecha_nacimiento():
        fecha_inicio = datetime(1950, 1, 1)
        fecha_fin = datetime(1980, 12, 31)
        # Generar un número aleatorio de días desde la fecha de inicio hasta la fecha de fin
        dias_aleatorios = random.randint(0, (fecha_fin - fecha_inicio).days)
        # Sumar ese número de días a la fecha de inicio para obtener una fecha aleatoria dentro del rango
        fecha_aleatoria = fecha_inicio + timedelta(days=dias_aleatorios)
        return fecha_aleatoria

    def generar_llamada_aleatorio():
        llamada_elegido = random.randint(1000, 10000)
        return f'{llamada_elegido}'
    
    def generar_peaje_gas_aleatorio():
        peaje_gas_elegido = random.randint(1000, 10000)
        return f'{peaje_gas_elegido}'
    
    def generar_peaje_gas_aleatorio():
        peaje_gas_elegido = random.randint(1000, 10000)
        return f'{peaje_gas_elegido}'
    
    def generar_peaje_gas_aleatorio():
        peaje_gas_elegido = random.randint(1000, 10000)
        return f'{peaje_gas_elegido}'
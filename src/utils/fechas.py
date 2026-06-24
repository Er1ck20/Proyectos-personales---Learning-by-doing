import pandas as pd

from src.config.logging_format import logger
''' 
# TODO - Crear una funcion para hacer ajustes de fechas de manera automatica
df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'])
df['fecha_apertura'] = pd.to_datetime(df['fecha_apertura'])
df['fecha_ultimo_pago'] = pd.to_datetime(df['fecha_ultimo_pago'])

'''
# Convertir fechas


def formateo_fechas(columna):
    logger.info("Función convertir_fecha ejecutada")
    return pd.to_datetime(columna,errors='coerce')

def obtener_anio(columna):
    logger.info("Obtener year ejecutada")
    return columna.dt.year
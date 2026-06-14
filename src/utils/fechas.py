import logging
import pandas as pd

logging.basicConfig(
    filename="database.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

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



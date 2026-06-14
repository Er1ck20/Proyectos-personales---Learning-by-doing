import logging
import pandas as pd

logging.basicConfig(
    filename="database.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

''' 
# TODO - Crear una funcion para hacer ajustes de fechas de manera automatica
df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'])
df['fecha_apertura'] = pd.to_datetime(df['fecha_apertura'])
df['fecha_ultimo_pago'] = pd.to_datetime(df['fecha_ultimo_pago'])

'''
def fechas(x):
    
    return pd.to_datetime(x)

print(fechas('10-apr-26'))


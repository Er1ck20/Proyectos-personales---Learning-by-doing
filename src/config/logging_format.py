'''   
Configuración centralizada del sistema de logging.

Define el logger de la aplicación y los handlers para
consola y archivo.
'''

# Importamos
import logging
from pathlib import Path

# Directorio donde se almacenarán los logs de la aplicación
LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
# Crearmos la carpeta si no existe
LOG_DIR.mkdir(exist_ok=True)

# Creamos el logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) # Define qué mensajes aceptará

# Lo formateamos
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
) # fecha_hora - nombre del logger - el nivel - el mensaje

# Un Handler es un destino.
console_handler = logging.StreamHandler()
# Formato del handler
console_handler.setFormatter(formatter) # Todo lo que salga por consola tendrá ese formato.

# Otro destino, es el filehandler
file_handler = logging.FileHandler(
    LOG_DIR / "app.log", # ruta
    encoding="utf-8" # codificacion
)
# Definimos el formato
file_handler.setFormatter(formatter)

# Agregar handlers hacia los dos destinos
logger.addHandler(console_handler)
logger.addHandler(file_handler)
import keyring
import oracledb
import os
import logging
from dotenv import load_dotenv

logging.basicConfig(
    filename="database.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding='utf-8'
)

logger = logging.getLogger(__name__)

# Cargar variables del .env
load_dotenv()

class DbAction:

    def __init__(self, connection_name):

        prefix = connection_name

        self.connection = None
        self.cursor = None

        self.username = os.getenv(f'{prefix}_USER')
        self.host = os.getenv(f'{prefix}_HOST')
        self.port = os.getenv(f'{prefix}_PORT')
        self.service_name = os.getenv(f'{prefix}_SERVICE')

        # Traemos la password desde el Credential Manager
        self.password = keyring.get_password(prefix, self.username)

        # Si no encontramos la pass
        if not self.password:
            raise ValueError("No se encontró la password en el Credential Manager") # Error si no encontramos la pass

    # Funcion conectar
    def conectar(self): 

        try:
            dsn = oracledb.makedsn(
                self.host,
                self.port,
                service_name=self.service_name
            )

            self.connection = oracledb.connect(
                user=self.username,
                password=self.password,
                dsn=dsn
            )

            # self.cursor = self.connection.cursor()

            logger.info("Conexión exitosa")
            return self.connection

        except oracledb.Error as e:
            logger.exception(f"Error al conectar: {e}")
            raise
            
    def cerrar(self):

        try:
            if self.cursor:
                self.cursor.close()

            if self.connection:
                self.connection.close()

            logger.info("Conexión cerrada")

        except Exception as e:
            logger.exception(f"Error cerrando conexión: {e}")
            raise
    
    def insertar(self):
        pass
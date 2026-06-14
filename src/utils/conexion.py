import keyring
import oracledb
import os
import logging
from dotenv import load_dotenv

logging.basicConfig(
    filename="database.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Cargar variables del .env
load_dotenv()

class database:
    def __init__(self, connection_name):

        prefix = connection_name

        self.connection = None
        self.cursor = None

        self.username = os.getenv(f'{prefix}_user')
        self.host = os.getenv(f'{prefix}_host')
        self.port = os.getenv(f'{prefix}_port')
        self.service_name = os.getenv(f'{prefix}_service')

        # Traemos la password desde el Credential Manager
        self.password = keyring.get_password(prefix, self.username)

        # Si no encontramos la pass
        if not self.password:
            raise ValueError("No se encontró la password en Credential Manager") # Error si no encontramos la pass

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
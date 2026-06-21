import logging

logging.basicConfig(
    filename="database.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Crear el logger
logger = logging.getLogger('ConsolaLogger')
logger.setLevel(logging.INFO)

# Formato comun
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Handler para consola
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

# Hnadler para archivo
file_handler = logging.FileHandler("ruta", encoding='utf-8')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
import logging

logging.basicConfig(
    filename="logs/errores.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def registrar_error(error):
    logging.error(str(error))

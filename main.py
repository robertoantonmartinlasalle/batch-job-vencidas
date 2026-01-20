# Este módulo Logging nos permite registrar mensajes (INFO, ERROR, etc.)
# en lugar de usar print(), que NO es apropiado para producción.
import logging

# Importar la función que lee y valida la configuración AS400
from core.config_loader import load_as400_config

# Importar la función responsable de crear la conexión ODBC.
from core.connection import create_as400_connection

# Se define la ruta del fichero de log.
LOG_FILE = "logs/batch_job.log"

"""
    Configura el sistema de logging del proyecto.

    Esta función debe llamarse UNA SOLA VEZ al inicio del programa.
    A partir de aquí, cualquier módulo podrá usar logging.getLogger(...)
    y escribir en el mismo sistema de logs.
    """

def setup_logging():
    # Nivel mínimo de log que se va a registrar. (INFO, WARNING, ERROR y CRITICAL)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s", # Formato del mensaje
        # Se definen dos "handlers": uno para fichero y otro para consola.
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )


def main():
    """
    Función principal del batch.

    Actúa como orquestador:
    - inicializa el logging
    - carga la configuración
    - establece la conexión AS400
    - maneja errores a alto nivel
    """
    # A partir de este punto, logging funciona en todo el programa.
    setup_logging()
    logger = logging.getLogger(__name__)
    # Muy importante para auditoría y trazabilidad.
    logger.info("Starting batch job")

    try:
        config = load_as400_config()
        logger.info("AS400 configuration loaded")
        # Se abre la conexión
        connection = create_as400_connection(config)
        logger.info("AS400 connection established successfully")
        # Se cierra la conexión
        connection.close()
        logger.info("AS400 connection closed")
    # en producción sin acceso a consola.
    except Exception as exc:
        logger.error(f"Batch job failed: {exc}", exc_info=True)


if __name__ == "__main__":
    main()

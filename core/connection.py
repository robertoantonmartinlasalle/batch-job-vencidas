import pyodbc
import logging

logger = logging.getLogger(__name__)


def create_as400_connection(config: dict):
    logger.info("Attempting AS400 connection")

    connection_string = (
        f"DRIVER={{{config['driver']}}};"
        f"SYSTEM={config['host']};"
        f"UID={config['user']};"
        f"PWD={config['password']};"
    )

    try:
        connection = pyodbc.connect(connection_string, timeout=5)
        return connection

    except pyodbc.Error as exc:
        logger.error("AS400 connection failed")
        raise RuntimeError("Unable to connect to AS400") from exc

import logging
from typing import Iterable, Optional

from core.sql.validator import validate_sql

logger = logging.getLogger(__name__)


def execute_select(
    connection,
    sql: str,
    params: Optional[Iterable] = None # Para permitir múltiples parámetros
):
    """
    Ejecuta una consulta SELECT de forma segura.

    - Valida el SQL antes de ejecutarlo
    - Usa sentencias preparadas (placeholders ?)
    - NO permite modificaciones de datos
    - Devuelve todas las filas resultantes
    """

    # Validamos la consulta (seguridad estructural)
    safe_sql = validate_sql(sql)

    try:
        cursor = connection.cursor()

        if params:
            logger.info("Executing SELECT with parameters")
            cursor.execute(safe_sql, params)
        else:
            logger.info("Executing SELECT without parameters")
            cursor.execute(safe_sql)

        # Recuperamos todas las filas
        rows = cursor.fetchall()

        return rows

    except Exception as exc:
        logger.error("Error executing SELECT", exc_info=True)
        raise

    finally:
        # Cerramos el cursor SIEMPRE
        cursor.close()

import re


# Palabras clave prohibidas (seguridad)
FORBIDDEN_KEYWORDS = (
    "insert",
    "update",
    "delete",
    "drop",
    "alter",
    "call",
    "exec",
    "truncate",
)


def validate_sql(sql: str) -> str:
    """
    Valida que una sentencia SQL sea estrictamente de solo lectura (SELECT).

    Reglas:
    - No puede estar vacía
    - Debe empezar por SELECT
    - No puede contener múltiples sentencias (;)
    - No puede contener palabras clave peligrosas
    - No puede contener comentarios SQL
    """

    if not isinstance(sql, str):
        raise ValueError("La consulta SQL debe ser una cadena de texto")

    # Se eliminan espacios en blanco al inicio y final
    normalized_sql = sql.strip()

    if not normalized_sql:
        raise ValueError("La consulta SQL está vacía")

    # Se normalizan a minúsculas para las comprobaciones
    sql_lower = normalized_sql.lower()

    # Debe empezar por SELECT
    if not sql_lower.startswith("select"):
        raise ValueError("Solo se permiten consultas SELECT")

    # No se permiten múltiples sentencias
    if ";" in sql_lower:
        raise ValueError("No se permiten múltiples sentencias SQL")

    # No se permiten comentarios SQL
    if "--" in sql_lower or "/*" in sql_lower or "*/" in sql_lower:
        raise ValueError("No se permiten comentarios en la consulta SQL")

    # Bloqueo de palabras clave peligrosas
    for keyword in FORBIDDEN_KEYWORDS:
        pattern = rf"\b{keyword}\b"
        if re.search(pattern, sql_lower):
            raise ValueError(f"Uso de palabra clave no permitida: {keyword}")

    # Si pasa todas las validaciones, devolvemos el SQL limpio
    return normalized_sql

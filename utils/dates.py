from datetime import date


def as400_yymmdd_to_date(value):
    """
    Convierte fechas AS400 DECIMAL(6) YYMMDD → datetime.date

    Ejemplo:
        260122 -> 2026-01-22

    Devuelve None si el valor es inválido.
    """
    if value is None:
        return None

    try:
        value = int(value)
        yy = value // 10000
        mm = (value // 100) % 100
        dd = value % 100

        year = 2000 + yy if yy < 70 else 1900 + yy
        return date(year, mm, dd)

    except Exception:
        return None

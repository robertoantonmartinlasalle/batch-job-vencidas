def normalize_factura(value):
    """
    Normaliza número de factura:
    - Evita notación científica (1.49e+06)
    - Devuelve siempre string legible
    """
    if value is None:
        return None

    try:
        return str(int(value))
    except Exception:
        return str(value)


def normalize_importe(value):
    """
    Normaliza importes AS400:
    - Decimal / float → float
    - Evita notación científica
    - Redondea a 2 decimales
    """
    if value is None:
        return 0.0

    try:
        return round(float(value), 2)
    except Exception:
        return 0.0

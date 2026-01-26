from datetime import date

from utils.dates import as400_yymmdd_to_date
from utils.normalizers import normalize_factura, normalize_importe


def process_facturas(rows, filter_year):
    """
    Aplica la lógica de negocio:
    - Filtro por año
    - Cálculo de pendiente
    - Estado de vencimiento
    """
    today = date.today()
    results = []

    for row in rows:
        fecha_factura = as400_yymmdd_to_date(row.get("FECHA_FACTURA"))
        if not fecha_factura or fecha_factura.year != filter_year:
            continue

        fecha_venc = as400_yymmdd_to_date(row.get("FECHA_VENCIMIENTO"))

        importe = normalize_importe(row.get("IMPORTE_FACTURA"))
        pagado = normalize_importe(row.get("IMPORTE_PAGADO"))
        pendiente = normalize_importe(importe - pagado)

        results.append({
            "anio": fecha_factura.year,
            "factura": normalize_factura(row.get("FACTURA")),
            "cliente": row.get("CLIENTE"),
            "importe": importe,
            "pagado": pagado,
            "pendiente": pendiente,
            "vencida": "SI" if fecha_venc and fecha_venc < today else "NO",
            "condiciones_pago": row.get("CONDICIONES_PAGO"),
            "fecha_factura": fecha_factura,
            "fecha_vencimiento": fecha_venc,
        })

    return results

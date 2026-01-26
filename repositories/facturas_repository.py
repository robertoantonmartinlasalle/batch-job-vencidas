from core.sql.executor import execute_select
from core.mappings.registry import get_mapping


def fetch_facturas(connection, max_rows):
    """
    Obtiene facturas desde AS400.
    SOLO acceso a datos (sin lógica de negocio).
    """
    mappings = get_mapping("facturas")

    HV_TABLE, HV_COLUMNS = mappings["hv"]
    OP_TABLE, OP_COLUMNS = mappings["op"]
    ADR_TABLE, ADR_COLUMNS = mappings["adr"]

    sql = f"""
        SELECT DISTINCT
            hv.{HV_COLUMNS['factura']}            AS FACTURA,
            hv.{HV_COLUMNS['condiciones_pago']}   AS CONDICIONES_PAGO,
            op.{OP_COLUMNS['fecha_factura']}      AS FECHA_FACTURA,
            op.{OP_COLUMNS['fecha_vencimiento']}  AS FECHA_VENCIMIENTO,
            op.{OP_COLUMNS['importe_factura']}    AS IMPORTE_FACTURA,
            op.{OP_COLUMNS['importe_pagado']}     AS IMPORTE_PAGADO,
            adr.{ADR_COLUMNS['nombre_comercial']} AS CLIENTE
        FROM {HV_TABLE['schema']}.{HV_TABLE['name']} hv
        INNER JOIN {OP_TABLE['schema']}.{OP_TABLE['name']} op
            ON op.{OP_COLUMNS['factura']} = hv.{HV_COLUMNS['factura']}
        INNER JOIN {ADR_TABLE['schema']}.{ADR_TABLE['name']} adr
            ON adr.{ADR_COLUMNS['id_direccion']} = hv.{HV_COLUMNS['deudor']}
        ORDER BY op.{OP_COLUMNS['fecha_factura']} DESC
        FETCH FIRST {max_rows} ROWS ONLY
    """

    rows = execute_select(connection, sql)

    if not rows:
        return []

    column_names = [col[0] for col in rows[0].cursor_description]
    return [dict(zip(column_names, row)) for row in rows]

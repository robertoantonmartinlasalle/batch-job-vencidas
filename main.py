import logging
import sys

from tabulate import tabulate

from core.config_loader import load_as400_config
from core.connection import create_as400_connection

from repositories.facturas_repository import fetch_facturas
from services.facturas_service import process_facturas


# ==================================================
# CONFIGURACIÓN
# ==================================================
LOG_FILE = "logs/batch_job.log"
FILTER_YEAR = 2026
MAX_ROWS = 100


def setup_logging():
    root_logger = logging.getLogger()
    if root_logger.handlers:
        return

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )


def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting batch job")

    preview_mode = "--preview" in sys.argv

    connection = None

    try:
        config = load_as400_config()
        connection = create_as400_connection(config)
        logger.info("AS400 connection established")

        rows = fetch_facturas(connection, MAX_ROWS)
        logger.info(f"Rows fetched: {len(rows)}")

        facturas = process_facturas(rows, FILTER_YEAR)
        logger.info(f"Facturas procesadas: {len(facturas)}")

        if preview_mode and facturas:
            print("\n=== FACTURAS ===\n")
            print(tabulate(
                [
                    (
                        f["anio"],
                        f["factura"],
                        f["cliente"],
                        f["importe"],
                        f["pagado"],
                        f["pendiente"],
                        f["vencida"],
                        f["condiciones_pago"],
                        f["fecha_factura"],
                        f["fecha_vencimiento"],
                    )
                    for f in facturas
                ],
                headers=[
                    "AÑO", "FACTURA", "CLIENTE",
                    "IMPORTE", "PAGADO", "PENDIENTE",
                    "VENCIDA", "COND. PAGO",
                    "FECHA FACTURA", "VENCIMIENTO"
                ],
                tablefmt="grid"
            ))
            print("\n=================\n")

    except Exception:
        logger.error("Batch job failed", exc_info=True)

    finally:
        if connection:
            connection.close()
            logger.info("AS400 connection closed")


if __name__ == "__main__":
    main()

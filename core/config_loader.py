import configparser
from pathlib import Path

CONFIG_PATH = Path("config/as400.ini")


def load_as400_config():
    if not CONFIG_PATH.exists():
        raise RuntimeError("No se encuentra config/as400.ini")

    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)

    if "as400" not in config:
        raise RuntimeError("Falta la sección [as400]")

    section = config["as400"]

    required = ("host", "driver", "user", "pass")
    for key in required:
        if key not in section or not section[key]:
            raise RuntimeError(f"Configuración AS400 incompleta: falta {key}")

    #  NORMALIZACIÓN (CLAVE)
    return {
        "host": section["host"],
        "driver": section["driver"],
        "user": section["user"],
        "password": section["pass"],
    }

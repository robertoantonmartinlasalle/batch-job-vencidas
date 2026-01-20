from core.config_loader import load_as400_config

cfg = load_as400_config()
print("Configuración cargada correctamente")
print("Host:", cfg["host"])
print("Driver:", cfg["driver"])

# Batch Job – Control de Facturación Vencida (AS400)

## Descripción

Este proyecto implementa un proceso **batch en Python** destinado al análisis de **facturas vencidas** a partir de datos obtenidos de un sistema **IBM i / AS400**, funcionando **exclusivamente en modo lectura**.

El objetivo principal es generar informes automáticos y facilitar la notificación a los equipos administrativos, sin comprometer la integridad del sistema AS400.

---

## Características principales

- Conexión a AS400 **solo lectura**
- Ejecución de consultas **SELECT únicamente**
- Análisis de facturación vencida
- Generación de informes (Excel)
- Preparado para ejecución automática (Task Scheduler / Cron)
- Arquitectura orientada a seguridad y trazabilidad

---

## Requisitos

- Python 3.10 o 3.11
- Driver **IBM i Access ODBC** instalado a nivel de sistema
- Acceso de red al AS400
- Usuario AS400 con permisos limitados

Las dependencias Python se gestionan mediante `requirements.txt`.

---

## Ejecución básica

1. Crear y activar el entorno virtual
2. Instalar dependencias
3. Configurar credenciales AS400
4. Ejecutar el batch

```bash
python main.py
```
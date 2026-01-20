# Batch Job – Control de Facturación Vencida (AS400)

## Descripción general

Este proyecto implementa un proceso batch desarrollado en Python cuyo objetivo es:

- Conectarse exclusivamente en modo lectura a un sistema IBM i / AS400
- Analizar facturas vencidas
- Generar informes en formato Excel
- Enviar notificaciones por correo a administración
- (Fase 2) Gestionar cuentas especiales con pagos agrupados

Bajo ningún concepto el sistema AS400 debe ser modificado.

El programa está diseñado para ejecutar únicamente consultas SELECT, con protecciones adicionales a nivel de software.

---

## Software obligatorio

- Python 3.10 o 3.11 (recomendado)

Motivo: compatibilidad estable con pyodbc y librerías estándar.

Verificación:

```bash
py --version
```
---

## Driver ODBC IBM i (AS400)

Debe estar instalado previamente en el servidor:

- IBM i Access ODBC Driver
- Versión compatible con el AS400 corporativo

Este driver es externo a Python y debe instalarse antes de ejecutar el batch.

---

## Conectividad con AS400

El servidor debe poder:

- Resolver el hostname del AS400
- Acceder por red
- Autenticarse con un usuario válido

---

## Usuario AS400

Requisitos del usuario técnico:

- Usuario dedicado al proceso batch
- Acceso únicamente a las tablas necesarias
- Idealmente permisos de solo lectura

El programa NO ejecuta:

- INSERT
- UPDATE
- DELETE
- CALL
- EXEC

Además, el código bloquea múltiples sentencias SQL por seguridad.

---

## Estructura del proyecto

    batch_job_vencidas/
    │
    ├── config/
    │   ├── as400.ini          # Credenciales reales (NO versionado)
    │   └── as400.ini.example  # Plantilla
    │
    ├── core/                  # Núcleo seguro del proyecto
    │
    ├── logs/                  # Logs de ejecución
    │
    ├── tests/                 # Tests de validación
    │
    ├── main.py                # Punto de entrada del batch
    ├── requirements.txt
    └── INSTALL.md

---

## Configuración de credenciales

### Archivo config/as400.ini

Este archivo NO debe subirse a control de versiones.

Ejemplo de contenido:

    [as400]
    host = AS400_HOST
    driver = IBM i Access ODBC Driver
    user = USUARIO
    pass = PASSWORD

Recomendaciones:

- Permisos restrictivos a nivel de sistema operativo
- Accesible únicamente por el usuario que ejecuta el batch
- Usuario AS400 con permisos mínimos

---

## Entorno virtual de Python (RECOMENDADO)

Crear entorno virtual:
```bash
py -m venv venv
```
Activar entorno en Windows:
```bash
venv\Scripts\activate
```
Activar entorno en Linux:
```bash
source venv/bin/activate
```
---

## Instalación de dependencias

Instalar dependencias:
```bash
pip install -r requirements.txt
```
Contenido mínimo recomendado de requirements.txt:

    pyodbc>=4.0,<5.0

Las dependencias deben instalarse directamente en el servidor de ejecución.

---

## Seguridad y garantías

El proyecto implementa las siguientes medidas:

- Credenciales fuera del código fuente
- Validación estricta del SQL (solo SELECT)
- Bloqueo de múltiples sentencias
- Logs de ejecución detallados
- Sin acceso web
- Sin entrada directa de usuario final

El sistema AS400 no puede verse modificado por este proceso.

---

## Ejecución en producción

El batch puede ejecutarse mediante:

- Task Scheduler (Windows)
- Cron (Linux)

Se recomienda ejecutar el proceso bajo un usuario de sistema dedicado.

---

## Mantenimiento

- Revisar logs periódicamente
- Validar cambios en estructuras AS400
- Probar siempre en entorno de pruebas
- No activar automatizaciones sin validación previa

import sys
from pathlib import Path
"""
Pytest no incluye automáticamente la raíz del proyecto en el PYTHONPATH,
lo que provoca fallos en imports absolutos como `core.*`.
Se añade explícitamente para permitir la correcta ejecución de los tests
sin afectar al código de producción.
"""
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/strategy
Fecha: 2025-10-21 23:16:16
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/strategy/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: absorcion_agua_strategy.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ================================================================================

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionAguaStrategy(ABC):
    """
    La interfaz del Patrón Strategy.
    Define el método que todas las estrategias de absorción de agua deben implementar.
    """
    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula la cantidad de agua que un cultivo debe absorber.

        Args:
            fecha (date): La fecha actual para cálculos estacionales.
            temperatura (float): La temperatura actual.
            humedad (float): La humedad actual.
            cultivo (Cultivo): El cultivo que está absorbiendo agua.

        Returns:
            int: La cantidad de agua absorbida en litros.
        """
        pass


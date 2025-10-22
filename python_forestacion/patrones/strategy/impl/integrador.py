"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/strategy/impl
Fecha: 2025-10-21 23:16:16
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/strategy/impl/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ================================================================================

from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorción constante, para hortalizas.
    Siempre absorbe la misma cantidad de agua.
    """
    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante

    def calcular_absorcion(self, fecha: date, temperatura: float, humedad: float, cultivo: 'Cultivo') -> int:
        return self._cantidad

# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ================================================================================

from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

# Valores que luego irán en constantes.py
MES_INICIO_VERANO = 3  # Marzo
MES_FIN_VERANO = 8   # Agosto
ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorción estacional, para árboles.
    Absorbe más agua en verano que en invierno.
    """
    def calcular_absorcion(self, fecha: date, temperatura: float, humedad: float, cultivo: 'Cultivo') -> int:
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO


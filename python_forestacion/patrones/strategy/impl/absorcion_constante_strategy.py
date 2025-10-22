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
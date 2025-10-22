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
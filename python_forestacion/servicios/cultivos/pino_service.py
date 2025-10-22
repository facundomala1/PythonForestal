from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino

class PinoService(ArbolService):
    """Servicio específico para el cultivo de Pino."""
    def __init__(self):
        # Inyectamos la estrategia estacional para los pinos.
        super().__init__(AbsorcionSeasonalStrategy())

    def mostrar_datos(self, cultivo: 'Pino') -> None:
        super().mostrar_datos(cultivo)
        print(f"  Variedad: {cultivo.get_variedad()}")
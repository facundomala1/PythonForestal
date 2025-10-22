from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo

class OlivoService(ArbolService):
    """Servicio específico para el cultivo de Olivo."""
    def __init__(self):
        # Los olivos también usan la estrategia estacional.
        super().__init__(AbsorcionSeasonalStrategy())

    def mostrar_datos(self, cultivo: 'Olivo') -> None:
        super().mostrar_datos(cultivo)
        print(f"  Tipo de aceituna: {cultivo.get_tipo_aceituna().name}")
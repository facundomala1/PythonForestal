from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

# Valor que luego irá a constantes.py
ABSORCION_LECHUGA = 1

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga

class LechugaService(CultivoService):
    """Servicio específico para el cultivo de Lechuga."""
    def __init__(self):
        # Inyectamos la estrategia constante para las lechugas.
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_LECHUGA))

    def mostrar_datos(self, cultivo: 'Lechuga') -> None:
        super().mostrar_datos(cultivo)
        print(f"  Variedad: {cultivo.get_variedad()}")
        print(f"  Invernadero: {'Sí' if cultivo.necesita_invernadero() else 'No'}")
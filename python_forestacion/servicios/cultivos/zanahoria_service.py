from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

# Valor que luego irá a constantes.py
ABSORCION_ZANAHORIA = 2

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class ZanahoriaService(CultivoService):
    """Servicio específico para el cultivo de Zanahoria."""
    def __init__(self):
        # Las zanahorias usan estrategia constante con un valor diferente.
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_ZANAHORIA))

    def mostrar_datos(self, cultivo: 'Zanahoria') -> None:
        super().mostrar_datos(cultivo)
        print(f"  Tipo: {'Baby Carrot' if cultivo.es_baby_carrot() else 'Regular'}")
        print(f"  Invernadero: {'Sí' if cultivo.necesita_invernadero() else 'No'}")
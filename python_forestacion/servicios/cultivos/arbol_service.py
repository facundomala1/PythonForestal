from abc import abstractmethod
from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol
    from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class ArbolService(CultivoService):
    """
    Servicio base abstracto para los servicios de tipo Árbol.
    Añade la lógica de crecimiento.
    """
    def __init__(self, estrategia_absorcion: 'AbsorcionAguaStrategy'):
        super().__init__(estrategia_absorcion)

    def crecer(self, arbol: 'Arbol', metros: float):
        """Aumenta la altura de un árbol."""
        if metros > 0:
            nueva_altura = arbol.get_altura() + metros
            arbol.set_altura(nueva_altura)

    @abstractmethod
    def mostrar_datos(self, cultivo: 'Arbol') -> None:
        super().mostrar_datos(cultivo)
        print(f"  ID: {cultivo.get_id()}")
        print(f"  Altura: {cultivo.get_altura():.2f} m")
from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class CultivoService(ABC):
    """
    Servicio base abstracto para todos los servicios de cultivo.
    Contiene la lógica común, como la absorción de agua, que delega a una Estrategia.
    """
    def __init__(self, estrategia_absorcion: 'AbsorcionAguaStrategy'):
        """
        Args:
            estrategia_absorcion (AbsorcionAguaStrategy): La estrategia de absorción de agua a utilizar.
        """
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: 'Cultivo') -> int:
        """
        Calcula y aplica la absorción de agua para un cultivo usando la estrategia inyectada.
        """
        # Simulamos valores de ambiente, ya que este servicio no tiene acceso directo a los sensores.
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            fecha=date.today(),
            temperatura=15.0,  # Valor simulado
            humedad=50.0,      # Valor simulado
            cultivo=cultivo
        )
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida

    @abstractmethod
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Muestra los datos básicos de un cultivo."""
        print(f"Cultivo: {type(cultivo).__name__}")
        print(f"  Superficie: {cultivo.get_superficie()} m²")
        print(f"  Agua almacenada: {cultivo.get_agua()} L")
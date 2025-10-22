from abc import ABC, abstractmethod
from typing import Generic, TypeVar

# TypeVar nos permite crear clases genéricas. 'T' puede ser cualquier tipo (float, str, etc.).
T = TypeVar('T')

class Observer(Generic[T], ABC):
    """
    La interfaz del Observador (Observer).
    Define el método 'actualizar' que será llamado por el Observable cuando haya un cambio.
    """
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Recibe una notificación del Observable.

        Args:
            evento (T): El dato o evento enviado por el Observable.
        """
        pass
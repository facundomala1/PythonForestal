from typing import Generic, TypeVar, List
from python_forestacion.patrones.observer.observer import Observer

T = TypeVar('T')

class Observable(Generic[T]):
    """
    La clase base del Sujeto (Observable).
    Mantiene una lista de observadores y les notifica de los cambios.
    """
    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """Añade un observador a la lista de suscriptores."""
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """Elimina un observador de la lista."""
        self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """Envía una notificación (evento) a todos los observadores suscritos."""
        for observador in self._observadores:
            observador.actualizar(evento)
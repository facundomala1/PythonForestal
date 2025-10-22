"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/observer
Fecha: 2025-10-21 23:16:16
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/observer/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/observer/observable.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/observer/observer.py
# ================================================================================

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


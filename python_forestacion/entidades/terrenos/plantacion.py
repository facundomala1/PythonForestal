from typing import List, TYPE_CHECKING

# Esto es para evitar errores de importación circular, una buena práctica.
if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador

# Valor que luego irá en constantes.py
AGUA_INICIAL_PLANTACION = 500

class Plantacion:
    """
    Entidad que representa la plantación, conteniendo cultivos, trabajadores
    y recursos como el agua.
    """
    def __init__(self, nombre: str, superficie: float):
        """
        Args:
            nombre (str): El nombre de la plantación (ej. "Finca del Madero").
            superficie (float): La superficie total disponible.
        """
        self._nombre = nombre
        self._superficie_total = superficie
        self._superficie_ocupada = 0.0
        self._agua_disponible = AGUA_INICIAL_PLANTACION
        self._cultivos: List['Cultivo'] = []
        self._trabajadores: List['Trabajador'] = []

    def get_nombre(self) -> str:
        return self._nombre

    def get_superficie_disponible(self) -> float:
        return self._superficie_total - self._superficie_ocupada

    def get_agua_disponible(self) -> int:
        return self._agua_disponible

    def set_agua_disponible(self, agua: int) -> None:
        if agua < 0:
            raise ValueError("El agua disponible no puede ser negativa.")
        self._agua_disponible = agua

    def get_cultivos(self) -> List['Cultivo']:
        # Devolvemos una copia para proteger la lista original (encapsulación)
        return self._cultivos.copy()

    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        self._cultivos.append(cultivo)
        self._superficie_ocupada += cultivo.get_superficie()

    def get_trabajadores(self) -> List['Trabajador']:
        return self._trabajadores.copy()

    def set_trabajadores(self, trabajadores: List['Trabajador']) -> None:
        self._trabajadores = trabajadores
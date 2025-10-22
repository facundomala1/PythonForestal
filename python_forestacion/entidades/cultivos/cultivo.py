from abc import ABC, abstractmethod

class Cultivo(ABC):
    """
    Clase base abstracta para todos los cultivos.
    Define la interfaz común que deben seguir todos los tipos de cultivos.
    """
    _id_counter = 0

    def __init__(self, superficie: float, agua: int):
        """
        Args:
            superficie (float): La superficie en m² que ocupa el cultivo.
            agua (int): La cantidad de agua inicial que almacena el cultivo.
        """
        Cultivo._id_counter += 1
        self._id = Cultivo._id_counter
        self._superficie = superficie
        self._agua = agua

    def get_id(self) -> int:
        return self._id

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        if superficie <= 0:
            raise ValueError("La superficie debe ser un valor positivo.")
        self._superficie = superficie

    def get_agua(self) -> int:
        return self._agua

    def set_agua(self, agua: int) -> None:
        if agua < 0:
            raise ValueError("El agua no puede ser negativa.")
        self._agua = agua

    @abstractmethod
    def __str__(self) -> str:
        """Devuelve una representación en cadena del cultivo."""
        pass
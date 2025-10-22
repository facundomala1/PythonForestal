from abc import abstractmethod
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo):
    """
    Clase base abstracta para cultivos de tipo Árbol.
    Hereda de Cultivo y añade el atributo de altura.
    """
    def __init__(self, superficie: float, agua: int, altura: float):
        super().__init__(superficie, agua)
        self._altura = altura

    def get_altura(self) -> float:
        return self._altura

    def set_altura(self, altura: float) -> None:
        if altura < 0:
            raise ValueError("La altura no puede ser negativa.")
        self._altura = altura

    @abstractmethod
    def __str__(self) -> str:
        pass
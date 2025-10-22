from abc import abstractmethod
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Hortaliza(Cultivo):
    """
    Clase base abstracta para cultivos de tipo Hortaliza.
    Hereda de Cultivo y añade el atributo de invernadero.
    """
    def __init__(self, superficie: float, agua: int, invernadero: bool):
        super().__init__(superficie, agua)
        self._invernadero = invernadero

    def necesita_invernadero(self) -> bool:
        return self._invernadero

    @abstractmethod
    def __str__(self) -> str:
        pass
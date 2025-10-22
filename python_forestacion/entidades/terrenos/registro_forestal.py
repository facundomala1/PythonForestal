from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion

class RegistroForestal:
    """
    Entidad que agrupa toda la información de una finca: el terreno,
    la plantación, el propietario y su avalúo.
    """
    def __init__(self, id_padron: int, tierra: 'Tierra', plantacion: 'Plantacion', propietario: str, avaluo: float):
        """
        Args:
            id_padron (int): El ID único del padrón.
            tierra (Tierra): El objeto Tierra asociado.
            plantacion (Plantacion): El objeto Plantacion asociado.
            propietario (str): El nombre del propietario.
            avaluo (float): El avalúo fiscal de la propiedad.
        """
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo

    def get_id_padron(self) -> int:
        return self._id_padron

    def get_tierra(self) -> 'Tierra':
        return self._tierra

    def get_plantacion(self) -> 'Plantacion':
        return self._plantacion

    def get_propietario(self) -> str:
        return self._propietario

    def get_avaluo(self) -> float:
        return self._avaluo
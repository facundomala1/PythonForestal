# Importamos TYPE_CHECKING para resolver dependencias circulares
from typing import TYPE_CHECKING

# Este bloque solo se ejecuta durante el análisis de tipos, no en tiempo de ejecución.
if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class Tierra:
    """
    Entidad que representa un terreno catastral con sus datos básicos.
    """
    def __init__(self, id_padron_catastral: int, superficie: float, domicilio: str):
        """
        Args:
            id_padron_catastral (int): El ID único del padrón.
            superficie (float): La superficie total del terreno en m².
            domicilio (str): La dirección o ubicación del terreno.
        """
        self._id_padron_catastral = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        # Una tierra tiene una finca o plantación asociada.
        self._finca: 'Plantacion' | None = None # Usamos None para indicar que puede no tener finca al inicio

    def get_id_padron_catastral(self) -> int:
        return self._id_padron_catastral

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        if superficie <= 0:
            raise ValueError("La superficie debe ser un valor positivo.")
        self._superficie = superficie

    def get_domicilio(self) -> str:
        return self._domicilio

    def set_domicilio(self, domicilio: str) -> None:
        self._domicilio = domicilio

    # Usamos comillas 'Plantacion' para la referencia a futuro
    def get_finca(self) -> 'Plantacion':
        return self._finca

    def set_finca(self, finca: 'Plantacion') -> None:
        self._finca = finca
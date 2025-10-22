from typing import TYPE_CHECKING
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion

class TierraService:
    """
    Servicio encargado de la lógica de negocio relacionada con la entidad Tierra.
    """
    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str
    ) -> Tierra:
        """
        Crea una instancia de Tierra y le asocia una nueva Plantacion.

        Args:
            id_padron_catastral (int): El ID del padrón del terreno.
            superficie (float): La superficie del terreno.
            domicilio (str): La ubicación del terreno.
            nombre_plantacion (str): El nombre para la plantación a crear.

        Returns:
            Tierra: El objeto Tierra creado y enlazado con su plantación.
        """
        tierra = Tierra(id_padron_catastral, superficie, domicilio)
        plantacion = Plantacion(nombre_plantacion, superficie)
        
        # Enlazamos la tierra con su plantación
        tierra.set_finca(plantacion)
        
        return tierra
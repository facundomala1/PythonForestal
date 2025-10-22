from typing import Dict, Type, List, TYPE_CHECKING
from python_forestacion.servicios.negocio.paquete import Paquete

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class FincasService:
    """
    Servicio de alto nivel para gestionar una colección de fincas (Registros Forestales).
    """
    def __init__(self):
        self._fincas: Dict[int, 'RegistroForestal'] = {}
        # Necesitaremos el servicio de plantación para algunas operaciones
        from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
        self._plantacion_service = PlantacionService()

    def add_finca(self, registro: 'RegistroForestal') -> None:
        """Agrega una finca (registro) al servicio."""
        id_padron = registro.get_id_padron()
        self._fincas[id_padron] = registro
        print(f"Finca con padrón {id_padron} agregada al servicio.")

    def buscar_finca(self, id_padron: int) -> 'RegistroForestal':
        """Busca y devuelve una finca por su ID de padrón."""
        finca = self._fincas.get(id_padron)
        if not finca:
            raise ValueError(f"No se encontró ninguna finca con el padrón {id_padron}.")
        return finca

    def fumigar(self, id_padron: int, plaguicida: str) -> None:
        """Fumiga la plantación de una finca específica."""
        finca = self.buscar_finca(id_padron)
        self._plantacion_service.fumigar(finca.get_plantacion(), plaguicida)

    def cosechar_yempaquetar(self, tipo_cultivo: Type['Cultivo']) -> Paquete['Cultivo']:
        """
        Cosecha todos los cultivos de un tipo específico de todas las fincas
        y los devuelve en un Paquete.
        """
        print(f"\nCOSECHANDO todas las unidades de {tipo_cultivo.__name__}...")
        
        cultivos_cosechados: List['Cultivo'] = []
        
        for finca in self._fincas.values():
            plantacion = finca.get_plantacion()
            cultivos_en_plantacion = plantacion.get_cultivos()
            
            # Filtramos los cultivos del tipo deseado
            a_cosechar = [c for c in cultivos_en_plantacion if isinstance(c, tipo_cultivo)]
            cultivos_cosechados.extend(a_cosechar)
            
            # Eliminamos los cultivos cosechados de la plantación (simulación)
            cultivos_restantes = [c for c in cultivos_en_plantacion if not isinstance(c, tipo_cultivo)]
            # Esto es una simplificación, una implementación real sería más compleja
            plantacion._cultivos = cultivos_restantes

        print(f"Se cosecharon un total de {len(cultivos_cosechados)} unidades.")

        # Empaquetamos la cosecha
        paquete = Paquete(tipo_cultivo)
        paquete.agregar_items(cultivos_cosechados)
        return paquete
"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/negocio
Fecha: 2025-10-21 23:16:16
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/negocio/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: fincas_service.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/negocio/fincas_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: paquete.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/negocio/paquete.py
# ================================================================================

from typing import List, TypeVar, Generic, Type

# T es una variable de tipo genérica. Puede representar cualquier clase.
T = TypeVar('T')

class Paquete(Generic[T]):
    """
    Una clase genérica que representa un paquete o caja de un tipo específico de cultivo.
    Utiliza Generics para garantizar la seguridad de tipos.
    """
    _id_counter = 0

    def __init__(self, tipo_contenido: Type[T]):
        """
        Args:
            tipo_contenido (Type[T]): El tipo de clase que contendrá el paquete.
        """
        Paquete._id_counter += 1
        self._id_paquete = Paquete._id_counter
        self._tipo_contenido = tipo_contenido
        self._contenido: List[T] = []

    def agregar_item(self, item: T) -> None:
        """Agrega un item al paquete, verificando que sea del tipo correcto."""
        if not isinstance(item, self._tipo_contenido):
            raise TypeError(f"Este paquete solo acepta {self._tipo_contenido.__name__}")
        self._contenido.append(item)

    def agregar_items(self, items: List[T]) -> None:
        """Agrega una lista de items al paquete."""
        for item in items:
            self.agregar_item(item)

    def mostrar_contenido_caja(self) -> None:
        """Muestra un resumen del contenido del paquete."""
        print("\n--- Contenido de la Caja ---")
        print(f"  ID Paquete: {self._id_paquete}")
        print(f"  Tipo:       {self._tipo_contenido.__name__}")
        print(f"  Cantidad:   {len(self._contenido)} unidades")
        print("----------------------------")


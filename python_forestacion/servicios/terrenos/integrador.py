"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/terrenos
Fecha: 2025-10-21 23:16:17
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/terrenos/plantacion_service.py
# ================================================================================

from typing import TYPE_CHECKING
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion

# Valores que luego irán a constantes.py
AGUA_RIEGO = 10
CRECIMIENTO_PINO = 0.10
CRECIMIENTO_OLIVO = 0.01

class PlantacionService:
    """
    Servicio con la lógica de negocio para las operaciones de una Plantacion.
    """
    def __init__(self):
        self._registry = CultivoServiceRegistry.get_instance()

    def plantar(self, plantacion: 'Plantacion', especie: str, cantidad: int) -> None:
        """
        Planta una cantidad de cultivos de una especie en la plantación.
        Utiliza el Patrón Factory para crear los cultivos.
        """
        # 1. Crear un cultivo temporal para saber cuánta superficie necesita
        cultivo_temporal = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_temporal.get_superficie() * cantidad

        # 2. Validar que haya superficie disponible
        if plantacion.get_superficie_disponible() < superficie_requerida:
            # Más adelante crearemos excepciones personalizadas
            raise ValueError("Superficie insuficiente para plantar.")

        # 3. Crear y agregar los cultivos
        for _ in range(cantidad):
            nuevo_cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.agregar_cultivo(nuevo_cultivo)
        
        print(f"Se plantaron {cantidad} unidades de {especie}.")

    def regar(self, plantacion: 'Plantacion') -> None:
        """
        Riega todos los cultivos de la plantación.
        Utiliza el Registry para delegar la absorción de agua.
        """
        # 1. Validar y consumir agua de la plantación
        if plantacion.get_agua_disponible() < AGUA_RIEGO:
            raise ValueError("Agua insuficiente en la plantación para regar.")
        
        plantacion.set_agua_disponible(plantacion.get_agua_disponible() - AGUA_RIEGO)
        
        # 2. Cada cultivo absorbe agua según su estrategia
        for cultivo in plantacion.get_cultivos():
            agua_absorbida = self._registry.absorver_agua(cultivo)
            print(f"El cultivo {cultivo.get_id()} ({type(cultivo).__name__}) absorbió {agua_absorbida}L de agua.")
            
            # Lógica de crecimiento específica
            from python_forestacion.entidades.cultivos.pino import Pino
            from python_forestacion.entidades.cultivos.olivo import Olivo
            if isinstance(cultivo, Pino):
                pino_service = self._registry.get_servicio(cultivo)
                pino_service.crecer(cultivo, CRECIMIENTO_PINO)
            elif isinstance(cultivo, Olivo):
                olivo_service = self._registry.get_servicio(cultivo)
                olivo_service.crecer(cultivo, CRECIMIENTO_OLIVO)

    def fumigar(self, plantacion: 'Plantacion', plaguicida: str) -> None:
        """Fumiga toda la plantación."""
        print(f"Fumigando la plantación '{plantacion.get_nombre()}' con {plaguicida}.")

    def mostrar_cultivos(self, plantacion: 'Plantacion') -> None:
        """Muestra los datos de todos los cultivos en la plantación."""
        print("\n--- Listado de Cultivos en la Plantación ---")
        for cultivo in plantacion.get_cultivos():
            self._registry.mostrar_datos(cultivo)
            print("-" * 20)

# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ================================================================================

import os
import pickle
from typing import TYPE_CHECKING

from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal

# Valores que luego irán a constantes.py
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

class RegistroForestalService:
    """
    Servicio para manejar la lógica de negocio del RegistroForestal,
    incluyendo la persistencia en disco y la visualización de datos.
    """
    def __init__(self):
        self._registry = CultivoServiceRegistry.get_instance()

    def mostrar_datos(self, registro: 'RegistroForestal') -> None:
        """Muestra un reporte completo y detallado del registro forestal."""
        plantacion = registro.get_plantacion()
        tierra = registro.get_tierra()

        print("\n=====================================")
        print("      REGISTRO FORESTAL COMPLETO")
        print("=====================================")
        print(f"Padrón Catastral: {registro.get_id_padron()}")
        print(f"Propietario:      {registro.get_propietario()}")
        print(f"Avalúo Fiscal:    ${registro.get_avaluo():,.2f}")
        print(f"Domicilio:        {tierra.get_domicilio()}")
        print(f"Superficie Total: {tierra.get_superficie()} m²")
        print(f"Cultivos Plantados: {len(plantacion.get_cultivos())} unidades")
        print("-------------------------------------")

        plantacion_service = PlantacionService()
        plantacion_service.mostrar_cultivos(plantacion)

    def _get_ruta_archivo(self, propietario: str) -> str:
        """Construye la ruta completa del archivo de persistencia."""
        nombre_archivo = f"{propietario}{EXTENSION_DATA}"
        return os.path.join(DIRECTORIO_DATA, nombre_archivo)

    def persistir(self, registro: 'RegistroForestal') -> None:
        """
        Guarda un objeto RegistroForestal en disco usando pickle.
        """
        propietario = registro.get_propietario()
        if not propietario:
            raise ValueError("El propietario no puede ser nulo o vacío para persistir.")

        # Asegurarse de que el directorio 'data' exista
        if not os.path.exists(DIRECTORIO_DATA):
            os.makedirs(DIRECTORIO_DATA)

        ruta_archivo = self._get_ruta_archivo(propietario)

        try:
            with open(ruta_archivo, 'wb') as f:
                pickle.dump(registro, f)
            print(f"Registro de '{propietario}' guardado exitosamente en '{ruta_archivo}'.")
        except IOError as e:
            # Más adelante crearemos una excepción personalizada
            raise Exception(f"Error al escribir en el archivo: {e}")

    @staticmethod
    def leer_registro(propietario: str) -> 'RegistroForestal':
        """
        Carga un objeto RegistroForestal desde un archivo.
        """
        if not propietario:
            raise ValueError("El nombre del propietario es necesario para leer el registro.")

        ruta_archivo = RegistroForestalService()._get_ruta_archivo(propietario)

        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"No se encontró el archivo de registro para '{propietario}'.")

        try:
            with open(ruta_archivo, 'rb') as f:
                registro = pickle.load(f)
            print(f"Registro de '{propietario}' cargado exitosamente desde '{ruta_archivo}'.")
            return registro
        except (pickle.UnpicklingError, IOError) as e:
            raise Exception(f"Error al leer o deserializar el archivo: {e}")

# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/terrenos/tierra_service.py
# ================================================================================

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


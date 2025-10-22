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
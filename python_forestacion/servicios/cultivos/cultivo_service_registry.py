from threading import Lock
from typing import Dict, TYPE_CHECKING

# Importaciones de entidades
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

# Importaciones de servicios
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

class CultivoServiceRegistry:
    """
    Un registro central para todos los servicios de cultivo.
    Implementa el patrón Singleton para garantizar una única instancia.
    Utiliza el patrón Registry para despachar operaciones al servicio correcto.
    """
    _instance = None
    _lock = Lock()  # Para asegurar que la creación de la instancia sea thread-safe

    def __new__(cls):
        # Lógica del Singleton
        if cls._instance is None:
            with cls._lock:
                # Double-checked locking para eficiencia
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    # Inicializamos los servicios solo una vez
                    cls._instance._inicializar_servicios()
        return cls._instance

    @classmethod
    def get_instance(cls):
        """Método de acceso principal a la instancia Singleton."""
        if cls._instance is None:
            cls()  # Llama a __new__ para crear la instancia si no existe
        return cls._instance

    def _inicializar_servicios(self):
        """Inicializa todos los servicios de cultivo y los mapeos."""
        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()

        # Mapeo de tipos de cultivo a sus servicios (Patrón Registry)
        self._servicios: Dict[type, 'CultivoService'] = {
            Pino: self._pino_service,
            Olivo: self._olivo_service,
            Lechuga: self._lechuga_service,
            Zanahoria: self._zanahoria_service
        }

    def get_servicio(self, cultivo: 'Cultivo') -> 'CultivoService':
        """
        Devuelve el servicio apropiado para un tipo de cultivo dado.
        """
        tipo_cultivo = type(cultivo)
        servicio = self._servicios.get(tipo_cultivo)
        if not servicio:
            raise TypeError(f"No hay un servicio registrado para el tipo {tipo_cultivo.__name__}")
        return servicio

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Delega la operación de mostrar datos al servicio correcto."""
        servicio = self.get_servicio(cultivo)
        servicio.mostrar_datos(cultivo)

    def absorver_agua(self, cultivo: 'Cultivo') -> int:
        """Delega la operación de absorber agua al servicio correcto."""
        servicio = self.get_servicio(cultivo)
        return servicio.absorver_agua(cultivo)
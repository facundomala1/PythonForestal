"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos
Fecha: 2025-10-21 23:16:16
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos/arbol_service.py
# ================================================================================

from abc import abstractmethod
from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol
    from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class ArbolService(CultivoService):
    """
    Servicio base abstracto para los servicios de tipo Árbol.
    Añade la lógica de crecimiento.
    """
    def __init__(self, estrategia_absorcion: 'AbsorcionAguaStrategy'):
        super().__init__(estrategia_absorcion)

    def crecer(self, arbol: 'Arbol', metros: float):
        """Aumenta la altura de un árbol."""
        if metros > 0:
            nueva_altura = arbol.get_altura() + metros
            arbol.set_altura(nueva_altura)

    @abstractmethod
    def mostrar_datos(self, cultivo: 'Arbol') -> None:
        super().mostrar_datos(cultivo)
        print(f"  ID: {cultivo.get_id()}")
        print(f"  Altura: {cultivo.get_altura():.2f} m")

# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos/cultivo_service.py
# ================================================================================

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class CultivoService(ABC):
    """
    Servicio base abstracto para todos los servicios de cultivo.
    Contiene la lógica común, como la absorción de agua, que delega a una Estrategia.
    """
    def __init__(self, estrategia_absorcion: 'AbsorcionAguaStrategy'):
        """
        Args:
            estrategia_absorcion (AbsorcionAguaStrategy): La estrategia de absorción de agua a utilizar.
        """
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: 'Cultivo') -> int:
        """
        Calcula y aplica la absorción de agua para un cultivo usando la estrategia inyectada.
        """
        # Simulamos valores de ambiente, ya que este servicio no tiene acceso directo a los sensores.
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            fecha=date.today(),
            temperatura=15.0,  # Valor simulado
            humedad=50.0,      # Valor simulado
            cultivo=cultivo
        )
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida

    @abstractmethod
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Muestra los datos básicos de un cultivo."""
        print(f"Cultivo: {type(cultivo).__name__}")
        print(f"  Superficie: {cultivo.get_superficie()} m²")
        print(f"  Agua almacenada: {cultivo.get_agua()} L")

# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos/lechuga_service.py
# ================================================================================

from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

# Valor que luego irá a constantes.py
ABSORCION_LECHUGA = 1

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga

class LechugaService(CultivoService):
    """Servicio específico para el cultivo de Lechuga."""
    def __init__(self):
        # Inyectamos la estrategia constante para las lechugas.
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_LECHUGA))

    def mostrar_datos(self, cultivo: 'Lechuga') -> None:
        super().mostrar_datos(cultivo)
        print(f"  Variedad: {cultivo.get_variedad()}")
        print(f"  Invernadero: {'Sí' if cultivo.necesita_invernadero() else 'No'}")

# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos/olivo_service.py
# ================================================================================

from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo

class OlivoService(ArbolService):
    """Servicio específico para el cultivo de Olivo."""
    def __init__(self):
        # Los olivos también usan la estrategia estacional.
        super().__init__(AbsorcionSeasonalStrategy())

    def mostrar_datos(self, cultivo: 'Olivo') -> None:
        super().mostrar_datos(cultivo)
        print(f"  Tipo de aceituna: {cultivo.get_tipo_aceituna().name}")

# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos/pino_service.py
# ================================================================================

from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino

class PinoService(ArbolService):
    """Servicio específico para el cultivo de Pino."""
    def __init__(self):
        # Inyectamos la estrategia estacional para los pinos.
        super().__init__(AbsorcionSeasonalStrategy())

    def mostrar_datos(self, cultivo: 'Pino') -> None:
        super().mostrar_datos(cultivo)
        print(f"  Variedad: {cultivo.get_variedad()}")

# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos/zanahoria_service.py
# ================================================================================

from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

# Valor que luego irá a constantes.py
ABSORCION_ZANAHORIA = 2

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class ZanahoriaService(CultivoService):
    """Servicio específico para el cultivo de Zanahoria."""
    def __init__(self):
        # Las zanahorias usan estrategia constante con un valor diferente.
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_ZANAHORIA))

    def mostrar_datos(self, cultivo: 'Zanahoria') -> None:
        super().mostrar_datos(cultivo)
        print(f"  Tipo: {'Baby Carrot' if cultivo.es_baby_carrot() else 'Regular'}")
        print(f"  Invernadero: {'Sí' if cultivo.necesita_invernadero() else 'No'}")


"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion
Fecha de generacion: 2025-10-21 23:16:17
Total de archivos integrados: 65
Total de directorios procesados: 21
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#
# DIRECTORIO: entidades
#   3. __init__.py
#
# DIRECTORIO: entidades/cultivos
#   4. __init.py
#   5. arbol.py
#   6. cultivo.py
#   7. hortaliza.py
#   8. lechuga.py
#   9. olivo.py
#   10. pino.py
#   11. tipo_aceituna.py
#   12. zanahoria.py
#
# DIRECTORIO: entidades/personal
#   13. __init__.py
#   14. apto_medico.py
#   15. herramienta.py
#   16. tarea.py
#   17. trabajador.py
#
# DIRECTORIO: entidades/terrenos
#   18. __init__.py
#   19. plantacion.py
#   20. registro_forestal.py
#   21. tierra.py
#
# DIRECTORIO: excepciones
#   22. __init__.py
#   23. agua_agotada_exception.py
#   24. forestacion_exception.py
#   25. persistencia_exception.py
#   26. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   27. __init__.py
#
# DIRECTORIO: patrones/factory
#   28. __init__.py
#   29. cultivo_factory.py
#
# DIRECTORIO: patrones/observer
#   30. __init__.py
#   31. observable.py
#   32. observer.py
#
# DIRECTORIO: patrones/observer/eventos
#   33. __init__.py
#   34. evento_plantacion.py
#   35. evento_sensor.py
#
# DIRECTORIO: patrones/singleton
#   36. __init.py
#
# DIRECTORIO: patrones/strategy
#   37. __init__.py
#   38. absorcion_agua_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#   39. __init__.py
#   40. absorcion_constante_strategy.py
#   41. absorcion_seasonal_strategy.py
#
# DIRECTORIO: riego
#   42. __init__.py
#
# DIRECTORIO: riego/control
#   43. __init__.py
#   44. control_riego_task.py
#
# DIRECTORIO: riego/sensores
#   45. __init__.py
#   46. humedad_reader_task.py
#   47. temperatura_reader_task.py
#
# DIRECTORIO: servicios
#   48. __init__.py
#
# DIRECTORIO: servicios/cultivos
#   49. __init__.py
#   50. arbol_service.py
#   51. cultivo_service.py
#   52. cultivo_service_registry.py
#   53. lechuga_service.py
#   54. olivo_service.py
#   55. pino_service.py
#   56. zanahoria_service.py
#
# DIRECTORIO: servicios/negocio
#   57. __init__.py
#   58. fincas_service.py
#   59. paquete.py
#
# DIRECTORIO: servicios/personal
#   60. __init__.py
#   61. trabajador_service.py
#
# DIRECTORIO: servicios/terrenos
#   62. __init__.py
#   63. plantacion_service.py
#   64. registro_forestal_service.py
#   65. tierra_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/65: __init__.py
# Directorio: .
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/65: constantes.py
# Directorio: .
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/constantes.py
# ==============================================================================

# ==============================================================================
# CONSTANTES DEL SISTEMA DE GESTION FORESTAL
# ==============================================================================

# ------------------------------------------------------------------------------
# Archivos y Persistencia
# ------------------------------------------------------------------------------
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"
THREAD_JOIN_TIMEOUT = 2.0  # segundos

# ------------------------------------------------------------------------------
# Terrenos y Plantaciones
# ------------------------------------------------------------------------------
AGUA_INICIAL_PLANTACION = 500  # litros
AGUA_RIEGO = 10                # litros consumidos por riego

# ------------------------------------------------------------------------------
# Cultivos: Pino
# ------------------------------------------------------------------------------
SUPERFICIE_PINO = 2.0          # m²
AGUA_INICIAL_PINO = 2          # litros
ALTURA_INICIAL_ARBOL = 1.0     # metros (usado por Pino)
CRECIMIENTO_PINO = 0.10        # metros por riego

# ------------------------------------------------------------------------------
# Cultivos: Olivo
# ------------------------------------------------------------------------------
SUPERFICIE_OLIVO = 3.0         # m²
AGUA_INICIAL_OLIVO = 5         # litros
ALTURA_INICIAL_OLIVO = 0.5     # metros
CRECIMIENTO_OLIVO = 0.01       # metros por riego

# ------------------------------------------------------------------------------
# Cultivos: Lechuga
# ------------------------------------------------------------------------------
SUPERFICIE_LECHUGA = 0.10      # m²
AGUA_INICIAL_LECHUGA = 1       # litros
ABSORCION_LECHUGA = 1          # litros

# ------------------------------------------------------------------------------
# Cultivos: Zanahoria
# ------------------------------------------------------------------------------
SUPERFICIE_ZANAHORIA = 0.15    # m²
AGUA_INICIAL_ZANAHORIA = 0     # litros
ABSORCION_ZANAHORIA = 2        # litros

# ------------------------------------------------------------------------------
# Sistema de Riego Automatizado
# ------------------------------------------------------------------------------
INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
SENSOR_TEMP_MIN = -25.0             # °C
SENSOR_TEMP_MAX = 50.0              # °C

INTERVALO_SENSOR_HUMEDAD = 3.0      # segundos
SENSOR_HUMEDAD_MIN = 0.0            # %
SENSOR_HUMEDAD_MAX = 100.0          # %

INTERVALO_CONTROL_RIEGO = 2.5       # segundos
TEMP_MIN_RIEGO = 8.0                # °C
TEMP_MAX_RIEGO = 15.0               # °C
HUMEDAD_MAX_RIEGO = 50.0            # %

# ------------------------------------------------------------------------------
# Estrategias de Absorción de Agua
# ------------------------------------------------------------------------------
MES_INICIO_VERANO = 3               # Marzo
MES_FIN_VERANO = 8                  # Agosto
ABSORCION_SEASONAL_VERANO = 5       # litros
ABSORCION_SEASONAL_INVIERNO = 2     # litros


################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 3/65: __init__.py
# Directorio: entidades
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 4/65: __init.py
# Directorio: entidades/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/__init.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 5/65: arbol.py
# Directorio: entidades/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/arbol.py
# ==============================================================================

from abc import abstractmethod
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo):
    """
    Clase base abstracta para cultivos de tipo Árbol.
    Hereda de Cultivo y añade el atributo de altura.
    """
    def __init__(self, superficie: float, agua: int, altura: float):
        super().__init__(superficie, agua)
        self._altura = altura

    def get_altura(self) -> float:
        return self._altura

    def set_altura(self, altura: float) -> None:
        if altura < 0:
            raise ValueError("La altura no puede ser negativa.")
        self._altura = altura

    @abstractmethod
    def __str__(self) -> str:
        pass

# ==============================================================================
# ARCHIVO 6/65: cultivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/cultivo.py
# ==============================================================================

from abc import ABC, abstractmethod

class Cultivo(ABC):
    """
    Clase base abstracta para todos los cultivos.
    Define la interfaz común que deben seguir todos los tipos de cultivos.
    """
    _id_counter = 0

    def __init__(self, superficie: float, agua: int):
        """
        Args:
            superficie (float): La superficie en m² que ocupa el cultivo.
            agua (int): La cantidad de agua inicial que almacena el cultivo.
        """
        Cultivo._id_counter += 1
        self._id = Cultivo._id_counter
        self._superficie = superficie
        self._agua = agua

    def get_id(self) -> int:
        return self._id

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        if superficie <= 0:
            raise ValueError("La superficie debe ser un valor positivo.")
        self._superficie = superficie

    def get_agua(self) -> int:
        return self._agua

    def set_agua(self, agua: int) -> None:
        if agua < 0:
            raise ValueError("El agua no puede ser negativa.")
        self._agua = agua

    @abstractmethod
    def __str__(self) -> str:
        """Devuelve una representación en cadena del cultivo."""
        pass

# ==============================================================================
# ARCHIVO 7/65: hortaliza.py
# Directorio: entidades/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/hortaliza.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 8/65: lechuga.py
# Directorio: entidades/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/lechuga.py
# ==============================================================================

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza

# Valores que luego irán en constantes.py
SUPERFICIE_LECHUGA = 0.10
AGUA_INICIAL_LECHUGA = 1

class Lechuga(Hortaliza):
    """
    Entidad Lechuga. Hereda de Hortaliza y representa un cultivo de lechuga.
    """
    def __init__(self, variedad: str):
        """
        Args:
            variedad (str): La variedad de la lechuga (ej. "Crespa", "Mantecosa").
        """
        super().__init__(
            superficie=SUPERFICIE_LECHUGA,
            agua=AGUA_INICIAL_LECHUGA,
            invernadero=True  # Las lechugas siempre van en invernadero
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad

    def __str__(self) -> str:
        return (f"Cultivo: Lechuga (ID: {self.get_id()})\n"
                f"  - Variedad: {self.get_variedad()}\n"
                f"  - Invernadero: {'Sí' if self.necesita_invernadero() else 'No'}\n"
                f"  - Agua: {self.get_agua()} L\n"
                f"  - Superficie: {self.get_superficie()} m²")

# ==============================================================================
# ARCHIVO 9/65: olivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/olivo.py
# ==============================================================================

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna

# Valores que luego irán en constantes.py
SUPERFICIE_OLIVO = 3.0
AGUA_INICIAL_OLIVO = 5
ALTURA_INICIAL_OLIVO = 0.5

class Olivo(Arbol):
    """
    Entidad Olivo. Hereda de Arbol y representa un cultivo de olivo.
    """
    def __init__(self, tipo_aceituna: TipoAceituna):
        """
        Args:
            tipo_aceituna (TipoAceituna): El tipo de aceituna del olivo.
        """
        super().__init__(
            superficie=SUPERFICIE_OLIVO,
            agua=AGUA_INICIAL_OLIVO,
            altura=ALTURA_INICIAL_OLIVO
        )
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        return self._tipo_aceituna

    def set_tipo_aceituna(self, tipo_aceituna: TipoAceituna) -> None:
        self._tipo_aceituna = tipo_aceituna

    def __str__(self) -> str:
        return (f"Cultivo: Olivo (ID: {self.get_id()})\n"
                f"  - Tipo Aceituna: {self.get_tipo_aceituna().name}\n"
                f"  - Altura: {self.get_altura():.2f} m\n"
                f"  - Agua: {self.get_agua()} L\n"
                f"  - Superficie: {self.get_superficie()} m²")

# ==============================================================================
# ARCHIVO 10/65: pino.py
# Directorio: entidades/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/pino.py
# ==============================================================================

from python_forestacion.entidades.cultivos.arbol import Arbol

# Valores que luego irán en constantes.py
SUPERFICIE_PINO = 2.0
AGUA_INICIAL_PINO = 2
ALTURA_INICIAL_ARBOL = 1.0

class Pino(Arbol):
    """
    Entidad Pino. Hereda de Arbol y representa un cultivo de pino.
    """
    def __init__(self, variedad: str):
        """
        Args:
            variedad (str): La variedad del pino (ej. "Parana", "Elliott").
        """
        super().__init__(
            superficie=SUPERFICIE_PINO,
            agua=AGUA_INICIAL_PINO,
            altura=ALTURA_INICIAL_ARBOL
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad

    def __str__(self) -> str:
        return (f"Cultivo: Pino (ID: {self.get_id()})\n"
                f"  - Variedad: {self.get_variedad()}\n"
                f"  - Altura: {self.get_altura():.2f} m\n"
                f"  - Agua: {self.get_agua()} L\n"
                f"  - Superficie: {self.get_superficie()} m²")

# ==============================================================================
# ARCHIVO 11/65: tipo_aceituna.py
# Directorio: entidades/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ==============================================================================

from enum import Enum, auto

class TipoAceituna(Enum):
    """
    Enumeración para los tipos de aceituna que puede tener un Olivo.
    """
    ARBEQUINA = auto()
    PICUAL = auto()
    MANZANILLA = auto()

# ==============================================================================
# ARCHIVO 12/65: zanahoria.py
# Directorio: entidades/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/zanahoria.py
# ==============================================================================

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza

# Valores que luego irán en constantes.py
SUPERFICIE_ZANAHORIA = 0.15
AGUA_INICIAL_ZANAHORIA = 0

class Zanahoria(Hortaliza):
    """
    Entidad Zanahoria. Hereda de Hortaliza y representa un cultivo de zanahoria.
    """
    def __init__(self, es_baby: bool):
        """
        Args:
            es_baby (bool): True si es una baby carrot, False si es regular.
        """
        super().__init__(
            superficie=SUPERFICIE_ZANAHORIA,
            agua=AGUA_INICIAL_ZANAHORIA,
            invernadero=False  # Las zanahorias no requieren invernadero
        )
        self._es_baby_carrot = es_baby

    def es_baby_carrot(self) -> bool:
        return self._es_baby_carrot

    def __str__(self) -> str:
        return (f"Cultivo: Zanahoria (ID: {self.get_id()})\n"
                f"  - Tipo: {'Baby Carrot' if self.es_baby_carrot() else 'Regular'}\n"
                f"  - Invernadero: {'Sí' if self.necesita_invernadero() else 'No'}\n"
                f"  - Agua: {self.get_agua()} L\n"
                f"  - Superficie: {self.get_superficie()} m²")


################################################################################
# DIRECTORIO: entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 13/65: __init__.py
# Directorio: entidades/personal
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 14/65: apto_medico.py
# Directorio: entidades/personal
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/personal/apto_medico.py
# ==============================================================================

from datetime import date

class AptoMedico:
    """
    Entidad que representa la certificación de aptitud médica de un trabajador.
    """
    def __init__(self, apto: bool, fecha_emision: date, observaciones: str = ""):
        """
        Args:
            apto (bool): True si el trabajador está apto, False si no.
            fecha_emision (date): La fecha en que se emitió el certificado.
            observaciones (str, optional): Comentarios adicionales del médico.
        """
        self._apto = apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones

    def esta_apto(self) -> bool:
        return self._apto

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def get_observaciones(self) -> str:
        return self._observaciones

# ==============================================================================
# ARCHIVO 15/65: herramienta.py
# Directorio: entidades/personal
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/personal/herramienta.py
# ==============================================================================

class Herramienta:
    """
    Entidad que representa una herramienta de trabajo.
    """
    def __init__(self, id_herramienta: int, nombre: str, certificado_hys: bool):
        """
        Args:
            id_herramienta (int): ID único de la herramienta.
            nombre (str): Nombre de la herramienta (ej. "Pala").
            certificado_hys (bool): True si tiene certificación de Higiene y Seguridad.
        """
        self._id_herramienta = id_herramienta
        self._nombre = nombre
        self._certificado_hys = certificado_hys

    def get_nombre(self) -> str:
        return self._nombre

# ==============================================================================
# ARCHIVO 16/65: tarea.py
# Directorio: entidades/personal
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/personal/tarea.py
# ==============================================================================

from datetime import date

class Tarea:
    """
    Entidad que representa una tarea asignada a un trabajador.
    """
    def __init__(self, id_tarea: int, fecha: date, descripcion: str):
        """
        Args:
            id_tarea (int): ID único de la tarea.
            fecha (date): Fecha programada para la tarea.
            descripcion (str): Descripción de la tarea (ej. "Desmalezar").
        """
        self._id_tarea = id_tarea
        self._fecha = fecha
        self._descripcion = descripcion
        self._completada = False

    def get_id_tarea(self) -> int:
        return self._id_tarea

    def get_fecha(self) -> date:
        return self._fecha

    def get_descripcion(self) -> str:
        return self._descripcion

    def esta_completada(self) -> bool:
        return self._completada

    def marcar_completada(self) -> None:
        self._completada = True

# ==============================================================================
# ARCHIVO 17/65: trabajador.py
# Directorio: entidades/personal
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/personal/trabajador.py
# ==============================================================================

from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.apto_medico import AptoMedico
    from python_forestacion.entidades.personal.tarea import Tarea

class Trabajador:
    """
    Entidad que representa a un trabajador con sus datos personales,
    tareas asignadas y su apto médico.
    """
    def __init__(self, dni: int, nombre: str, tareas: List['Tarea']):
        """
        Args:
            dni (int): DNI del trabajador.
            nombre (str): Nombre completo del trabajador.
            tareas (List[Tarea]): Lista de tareas iniciales asignadas.
        """
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas
        self._apto_medico: Optional['AptoMedico'] = None  # Un trabajador puede no tener apto al inicio

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def get_tareas(self) -> List['Tarea']:
        return self._tareas.copy()

    def get_apto_medico(self) -> Optional['AptoMedico']:
        return self._apto_medico

    def set_apto_medico(self, apto: 'AptoMedico') -> None:
        self._apto_medico = apto


################################################################################
# DIRECTORIO: entidades/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 18/65: __init__.py
# Directorio: entidades/terrenos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 19/65: plantacion.py
# Directorio: entidades/terrenos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/terrenos/plantacion.py
# ==============================================================================

from typing import List, TYPE_CHECKING

# Esto es para evitar errores de importación circular, una buena práctica.
if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador

# Valor que luego irá en constantes.py
AGUA_INICIAL_PLANTACION = 500

class Plantacion:
    """
    Entidad que representa la plantación, conteniendo cultivos, trabajadores
    y recursos como el agua.
    """
    def __init__(self, nombre: str, superficie: float):
        """
        Args:
            nombre (str): El nombre de la plantación (ej. "Finca del Madero").
            superficie (float): La superficie total disponible.
        """
        self._nombre = nombre
        self._superficie_total = superficie
        self._superficie_ocupada = 0.0
        self._agua_disponible = AGUA_INICIAL_PLANTACION
        self._cultivos: List['Cultivo'] = []
        self._trabajadores: List['Trabajador'] = []

    def get_nombre(self) -> str:
        return self._nombre

    def get_superficie_disponible(self) -> float:
        return self._superficie_total - self._superficie_ocupada

    def get_agua_disponible(self) -> int:
        return self._agua_disponible

    def set_agua_disponible(self, agua: int) -> None:
        if agua < 0:
            raise ValueError("El agua disponible no puede ser negativa.")
        self._agua_disponible = agua

    def get_cultivos(self) -> List['Cultivo']:
        # Devolvemos una copia para proteger la lista original (encapsulación)
        return self._cultivos.copy()

    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        self._cultivos.append(cultivo)
        self._superficie_ocupada += cultivo.get_superficie()

    def get_trabajadores(self) -> List['Trabajador']:
        return self._trabajadores.copy()

    def set_trabajadores(self, trabajadores: List['Trabajador']) -> None:
        self._trabajadores = trabajadores

# ==============================================================================
# ARCHIVO 20/65: registro_forestal.py
# Directorio: entidades/terrenos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/terrenos/registro_forestal.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 21/65: tierra.py
# Directorio: entidades/terrenos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/terrenos/tierra.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 22/65: __init__.py
# Directorio: excepciones
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/excepciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 23/65: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/excepciones/agua_agotada_exception.py
# ==============================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException

class AguaAgotadaException(ForestacionException):
    """Se lanza cuando no hay suficiente agua en la plantación para una operación."""
    def __init__(self, user_message: str, agua_requerida: int, agua_disponible: int):
        super().__init__(user_message)
        self.agua_requerida = agua_requerida
        self.agua_disponible = agua_disponible

# ==============================================================================
# ARCHIVO 24/65: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/excepciones/forestacion_exception.py
# ==============================================================================

class ForestacionException(Exception):
    """
    Clase base para todas las excepciones personalizadas del sistema.
    """
    def __init__(self, user_message: str, technical_message: str = ""):
        """
        Args:
            user_message (str): Un mensaje claro para el usuario final.
            technical_message (str, optional): Un mensaje con detalles técnicos para desarrolladores.
        """
        super().__init__(user_message)
        self.user_message = user_message
        self.technical_message = technical_message

    def get_user_message(self) -> str:
        return self.user_message

    def get_full_message(self) -> str:
        if self.technical_message:
            return f"{self.user_message} (Detalles técnicos: {self.technical_message})"
        return self.user_message

# ==============================================================================
# ARCHIVO 25/65: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/excepciones/persistencia_exception.py
# ==============================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException

class PersistenciaException(ForestacionException):
    """Se lanza cuando ocurre un error al leer o escribir archivos de persistencia."""
    def __init__(self, user_message: str, ruta_archivo: str, operacion: str):
        super().__init__(user_message)
        self.ruta_archivo = ruta_archivo
        self.operacion = operacion # 'lectura' o 'escritura'

# ==============================================================================
# ARCHIVO 26/65: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ==============================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """Se lanza cuando no hay suficiente superficie disponible para plantar."""
    def __init__(self, user_message: str, superficie_requerida: float, superficie_disponible: float):
        super().__init__(user_message)
        self.superficie_requerida = superficie_requerida
        self.superficie_disponible = superficie_disponible


################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 27/65: __init__.py
# Directorio: patrones
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 28/65: __init__.py
# Directorio: patrones/factory
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 29/65: cultivo_factory.py
# Directorio: patrones/factory
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/factory/cultivo_factory.py
# ==============================================================================

from typing import TYPE_CHECKING, Dict, Callable

# Para evitar importaciones circulares y mantener el código limpio
if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.cultivos.pino import Pino
    from python_forestacion.entidades.cultivos.olivo import Olivo
    from python_forestacion.entidades.cultivos.lechuga import Lechuga
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
    from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna

class CultivoFactory:
    """
    Patrón Factory Method para la creación de diferentes tipos de cultivos.
    Encapsula la lógica de instanciación para desacoplar el cliente de las clases concretas.
    """

    @staticmethod
    def _crear_pino() -> 'Pino':
        from python_forestacion.entidades.cultivos.pino import Pino
        # Por simplicidad, asignamos una variedad por defecto.
        return Pino(variedad="Parana")

    @staticmethod
    def _crear_olivo() -> 'Olivo':
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
        # Asignamos un tipo de aceituna por defecto.
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)

    @staticmethod
    def _crear_lechuga() -> 'Lechuga':
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        return Lechuga(variedad="Mantecosa")

    @staticmethod
    def _crear_zanahoria() -> 'Zanahoria':
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        # Creamos zanahorias regulares por defecto.
        return Zanahoria(es_baby=False)

    @staticmethod
    def crear_cultivo(especie: str) -> 'Cultivo':
        """
        El método fábrica principal.
        
        Args:
            especie (str): El nombre del tipo de cultivo a crear (ej. "Pino").

        Returns:
            Cultivo: Una instancia del cultivo solicitado.

        Raises:
            ValueError: Si la especie no es conocida por la fábrica.
        """
        # Usamos un diccionario para mapear nombres a funciones de creación.
        # Esto es más extensible que un if/elif/else.
        factories: Dict[str, Callable[[], 'Cultivo']] = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(f"Especie de cultivo desconocida: {especie}")

        # Llama a la función de creación correcta y devuelve el objeto.
        return factories[especie]()


################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 30/65: __init__.py
# Directorio: patrones/observer
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 31/65: observable.py
# Directorio: patrones/observer
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/observer/observable.py
# ==============================================================================

from typing import Generic, TypeVar, List
from python_forestacion.patrones.observer.observer import Observer

T = TypeVar('T')

class Observable(Generic[T]):
    """
    La clase base del Sujeto (Observable).
    Mantiene una lista de observadores y les notifica de los cambios.
    """
    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """Añade un observador a la lista de suscriptores."""
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """Elimina un observador de la lista."""
        self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """Envía una notificación (evento) a todos los observadores suscritos."""
        for observador in self._observadores:
            observador.actualizar(evento)

# ==============================================================================
# ARCHIVO 32/65: observer.py
# Directorio: patrones/observer
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/observer/observer.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

# TypeVar nos permite crear clases genéricas. 'T' puede ser cualquier tipo (float, str, etc.).
T = TypeVar('T')

class Observer(Generic[T], ABC):
    """
    La interfaz del Observador (Observer).
    Define el método 'actualizar' que será llamado por el Observable cuando haya un cambio.
    """
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Recibe una notificación del Observable.

        Args:
            evento (T): El dato o evento enviado por el Observable.
        """
        pass


################################################################################
# DIRECTORIO: patrones/observer/eventos
################################################################################

# ==============================================================================
# ARCHIVO 33/65: __init__.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/observer/eventos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 34/65: evento_plantacion.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 35/65: evento_sensor.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 36/65: __init.py
# Directorio: patrones/singleton
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/singleton/__init.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 37/65: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 38/65: absorcion_agua_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ==============================================================================

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionAguaStrategy(ABC):
    """
    La interfaz del Patrón Strategy.
    Define el método que todas las estrategias de absorción de agua deben implementar.
    """
    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula la cantidad de agua que un cultivo debe absorber.

        Args:
            fecha (date): La fecha actual para cálculos estacionales.
            temperatura (float): La temperatura actual.
            humedad (float): La humedad actual.
            cultivo (Cultivo): El cultivo que está absorbiendo agua.

        Returns:
            int: La cantidad de agua absorbida en litros.
        """
        pass


################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 39/65: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/strategy/impl/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 40/65: absorcion_constante_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ==============================================================================

from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorción constante, para hortalizas.
    Siempre absorbe la misma cantidad de agua.
    """
    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante

    def calcular_absorcion(self, fecha: date, temperatura: float, humedad: float, cultivo: 'Cultivo') -> int:
        return self._cantidad

# ==============================================================================
# ARCHIVO 41/65: absorcion_seasonal_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ==============================================================================

from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

# Valores que luego irán en constantes.py
MES_INICIO_VERANO = 3  # Marzo
MES_FIN_VERANO = 8   # Agosto
ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorción estacional, para árboles.
    Absorbe más agua en verano que en invierno.
    """
    def calcular_absorcion(self, fecha: date, temperatura: float, humedad: float, cultivo: 'Cultivo') -> int:
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO


################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 42/65: __init__.py
# Directorio: riego
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/riego/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: riego/control
################################################################################

# ==============================================================================
# ARCHIVO 43/65: __init__.py
# Directorio: riego/control
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/riego/control/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 44/65: control_riego_task.py
# Directorio: riego/control
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/riego/control/control_riego_task.py
# ==============================================================================

import threading
import time
from typing import TYPE_CHECKING
from python_forestacion.patrones.observer.observer import Observer

if TYPE_CHECKING:
    from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
    from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
    from python_forestacion.entidades.terrenos.plantacion import Plantacion

# Valores que luego irán a constantes.py
TEMP_MIN_RIEGO = 8.0
TEMP_MAX_RIEGO = 15.0
HUMEDAD_MAX_RIEGO = 50.0
INTERVALO_CONTROL_RIEGO = 2.5  # segundos

class ControlRiegoTask(threading.Thread, Observer[float]):
    """
    Controlador que se ejecuta en un hilo y observa los sensores para decidir
    cuándo regar la plantación. Es un Observer.
    """
    def __init__(
        self,
        sensor_temperatura: 'TemperaturaReaderTask',
        sensor_humedad: 'HumedadReaderTask',
        plantacion: 'Plantacion',
        plantacion_service: 'PlantacionService'
    ):
        threading.Thread.__init__(self, daemon=True)
        # Nota: No llamamos a super() de Observer porque no tiene __init__

        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        self._detenido = threading.Event()

        # Guardamos los últimos valores conocidos de los sensores
        self._ultima_temperatura: float = 20.0  # Valor inicial seguro
        self._ultima_humedad: float = 60.0    # Valor inicial seguro
        
        # Suscribirse a ambos sensores
        sensor_temperatura.agregar_observador(self)
        sensor_humedad.agregar_observador(self)

    def actualizar(self, evento: float) -> None:
        """
        Este método es llamado por CUALQUIER sensor (Observable).
        Aquí, inferimos si el dato es temperatura o humedad por su rango.
        Esta es una simplificación; un sistema real usaría un evento más complejo.
        """
        # Heurística para diferenciar el origen del dato
        from python_forestacion.riego.sensores.temperatura_reader_task import SENSOR_TEMP_MIN, SENSOR_TEMP_MAX
        if SENSOR_TEMP_MIN <= evento <= SENSOR_TEMP_MAX:
            self._ultima_temperatura = evento
        else: # Asumimos que es humedad si no encaja en el rango de temperatura
            self._ultima_humedad = evento

    def _evaluar_condiciones_riego(self):
        """Evalúa si se debe regar basado en los últimos datos de los sensores."""
        temp = self._ultima_temperatura
        hum = self._ultima_humedad

        print(f"[Control Riego]: Evaluando... Temp={temp}°C, Humedad={hum}%")

        if (TEMP_MIN_RIEGO <= temp <= TEMP_MAX_RIEGO) and (hum < HUMEDAD_MAX_RIEGO):
            print(f"[Control Riego]: CONDICIONES ÓPTIMAS. Iniciando riego...")
            try:
                self._plantacion_service.regar(self._plantacion)
                print("[Control Riego]: Riego completado exitosamente.")
            except ValueError as e:
                print(f"[Control Riego]: ERROR AL REGAR - {e}")
        else:
            print("[Control Riego]: Condiciones no aptas para riego. Esperando...")

    def run(self):
        """El código del hilo del controlador."""
        print("Control de Riego: INICIADO")
        while not self._detenido.is_set():
            self._evaluar_condiciones_riego()
            time.sleep(INTERVALO_CONTROL_RIEGO)
        print("Control de Riego: DETENIDO")

    def detener(self):
        """Señaliza al hilo que debe detenerse."""
        self._detenido.set()


################################################################################
# DIRECTORIO: riego/sensores
################################################################################

# ==============================================================================
# ARCHIVO 45/65: __init__.py
# Directorio: riego/sensores
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/riego/sensores/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 46/65: humedad_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/riego/sensores/humedad_reader_task.py
# ==============================================================================

import random
import time
import threading
from python_forestacion.patrones.observer.observable import Observable

# Valores que luego irán a constantes.py
INTERVALO_SENSOR_HUMEDAD = 3.0  # segundos
SENSOR_HUMEDAD_MIN = 0.0
SENSOR_HUMEDAD_MAX = 100.0

class HumedadReaderTask(threading.Thread, Observable[float]):
    """
    Un sensor que lee la humedad en un hilo separado.
    Actúa como un Observable, notificando a sus observadores de cada nueva lectura.
    """
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _leer_humedad(self) -> float:
        """Simula la lectura de un sensor de humedad."""
        return round(random.uniform(SENSOR_HUMEDAD_MIN, SENSOR_HUMEDAD_MAX), 2)

    def run(self):
        """El código que se ejecuta cuando el hilo comienza."""
        print("Sensor de Humedad: INICIADO")
        while not self._detenido.is_set():
            humedad = self._leer_humedad()
            print(f"[Sensor Humedad]: Nueva lectura -> {humedad}%")
            self.notificar_observadores(humedad)
            time.sleep(INTERVALO_SENSOR_HUMEDAD)
        print("Sensor de Humedad: DETENIDO")

    def detener(self):
        """Señaliza al hilo que debe detenerse."""
        self._detenido.set()

# ==============================================================================
# ARCHIVO 47/65: temperatura_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/riego/sensores/temperatura_reader_task.py
# ==============================================================================

import random
import time
import threading
from python_forestacion.patrones.observer.observable import Observable

# Valores que luego irán a constantes.py
INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
SENSOR_TEMP_MIN = -25.0
SENSOR_TEMP_MAX = 50.0

class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """
    Un sensor que lee la temperatura en un hilo separado.
    Actúa como un Observable, notificando a sus observadores de cada nueva lectura.
    """
    def __init__(self):
        # Es crucial llamar a los constructores de ambas clases padre
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _leer_temperatura(self) -> float:
        """Simula la lectura de un sensor de temperatura."""
        return round(random.uniform(SENSOR_TEMP_MIN, SENSOR_TEMP_MAX), 2)

    def run(self):
        """El código que se ejecuta cuando el hilo comienza (con .start())."""
        print("Sensor de Temperatura: INICIADO")
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            print(f"[Sensor Temp]: Nueva lectura -> {temperatura}°C")
            self.notificar_observadores(temperatura)
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)
        print("Sensor de Temperatura: DETENIDO")

    def detener(self):
        """Señaliza al hilo que debe detenerse de forma segura."""
        self._detenido.set()


################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 48/65: __init__.py
# Directorio: servicios
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 49/65: __init__.py
# Directorio: servicios/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 50/65: arbol_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos/arbol_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 51/65: cultivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos/cultivo_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 52/65: cultivo_service_registry.py
# Directorio: servicios/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 53/65: lechuga_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos/lechuga_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 54/65: olivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos/olivo_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 55/65: pino_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos/pino_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 56/65: zanahoria_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/cultivos/zanahoria_service.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 57/65: __init__.py
# Directorio: servicios/negocio
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/negocio/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 58/65: fincas_service.py
# Directorio: servicios/negocio
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/negocio/fincas_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 59/65: paquete.py
# Directorio: servicios/negocio
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/negocio/paquete.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 60/65: __init__.py
# Directorio: servicios/personal
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 61/65: trabajador_service.py
# Directorio: servicios/personal
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/personal/trabajador_service.py
# ==============================================================================

from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.entidades.personal.apto_medico import AptoMedico

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.trabajador import Trabajador
    from python_forestacion.entidades.personal.herramienta import Herramienta

class TrabajadorService:
    """
    Servicio para manejar la lógica de negocio relacionada con los trabajadores.
    """
    def asignar_apto_medico(
        self,
        trabajador: 'Trabajador',
        apto: bool,
        fecha_emision: date,
        observaciones: str = ""
    ) -> None:
        """
        Crea y asigna un certificado de AptoMedico a un trabajador.
        """
        apto_medico = AptoMedico(apto, fecha_emision, observaciones)
        trabajador.set_apto_medico(apto_medico)
        print(f"Se ha asignado el apto médico a '{trabajador.get_nombre()}'.")

    def trabajar(self, trabajador: 'Trabajador', fecha: date, herramienta: 'Herramienta') -> bool:
        """
        El trabajador ejecuta las tareas asignadas para una fecha específica,
        siempre y cuando tenga un apto médico válido.
        Las tareas se ejecutan en orden descendente de ID.
        """
        apto_medico = trabajador.get_apto_medico()
        
        # 1. Verificar si el trabajador puede trabajar
        if apto_medico is None or not apto_medico.esta_apto():
            print(f"El trabajador '{trabajador.get_nombre()}' NO puede trabajar. Falta apto médico o no es válido.")
            return False

        print(f"\nEl trabajador '{trabajador.get_nombre()}' comienza a trabajar con la herramienta '{herramienta.get_nombre()}':")
        
        # 2. Filtrar tareas para la fecha y que no estén completadas
        tareas_del_dia = [
            t for t in trabajador.get_tareas()
            if t.get_fecha() == fecha and not t.esta_completada()
        ]
        
        # 3. Ordenar tareas por ID descendente
        tareas_ordenadas = sorted(tareas_del_dia, key=lambda t: t.get_id_tarea(), reverse=True)

        if not tareas_ordenadas:
            print(f"No hay tareas pendientes para '{trabajador.get_nombre()}' en la fecha {fecha}.")
            return True

        # 4. Ejecutar tareas
        for tarea in tareas_ordenadas:
            print(f"  - Realizando tarea {tarea.get_id_tarea()}: '{tarea.get_descripcion()}'...")
            tarea.marcar_completada()
            
        return True


################################################################################
# DIRECTORIO: servicios/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 62/65: __init__.py
# Directorio: servicios/terrenos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 63/65: plantacion_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/terrenos/plantacion_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 64/65: registro_forestal_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 65/65: tierra_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/terrenos/tierra_service.py
# ==============================================================================

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


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 65
# Generado: 2025-10-21 23:16:17
################################################################################

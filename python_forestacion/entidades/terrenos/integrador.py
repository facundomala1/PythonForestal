"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/terrenos
Fecha: 2025-10-21 23:16:16
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/terrenos/plantacion.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/terrenos/registro_forestal.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/terrenos/tierra.py
# ================================================================================

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


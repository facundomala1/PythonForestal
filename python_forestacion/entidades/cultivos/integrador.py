"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos
Fecha: 2025-10-21 23:16:16
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/__init.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/arbol.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/cultivo.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/hortaliza.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/lechuga.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/olivo.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/pino.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ================================================================================

from enum import Enum, auto

class TipoAceituna(Enum):
    """
    Enumeración para los tipos de aceituna que puede tener un Olivo.
    """
    ARBEQUINA = auto()
    PICUAL = auto()
    MANZANILLA = auto()

# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/cultivos/zanahoria.py
# ================================================================================

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


"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/personal
Fecha: 2025-10-21 23:16:16
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/personal/apto_medico.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/personal/herramienta.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/personal/tarea.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/entidades/personal/trabajador.py
# ================================================================================

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


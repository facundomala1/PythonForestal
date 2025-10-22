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
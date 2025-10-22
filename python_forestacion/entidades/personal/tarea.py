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
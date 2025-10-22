"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/personal
Fecha: 2025-10-21 23:16:16
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: trabajador_service.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/servicios/personal/trabajador_service.py
# ================================================================================

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


"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/excepciones
Fecha: 2025-10-21 23:16:16
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/excepciones/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: agua_agotada_exception.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/excepciones/agua_agotada_exception.py
# ================================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException

class AguaAgotadaException(ForestacionException):
    """Se lanza cuando no hay suficiente agua en la plantación para una operación."""
    def __init__(self, user_message: str, agua_requerida: int, agua_disponible: int):
        super().__init__(user_message)
        self.agua_requerida = agua_requerida
        self.agua_disponible = agua_disponible

# ================================================================================
# ARCHIVO 3/5: forestacion_exception.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/excepciones/forestacion_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/5: persistencia_exception.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/excepciones/persistencia_exception.py
# ================================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException

class PersistenciaException(ForestacionException):
    """Se lanza cuando ocurre un error al leer o escribir archivos de persistencia."""
    def __init__(self, user_message: str, ruta_archivo: str, operacion: str):
        super().__init__(user_message)
        self.ruta_archivo = ruta_archivo
        self.operacion = operacion # 'lectura' o 'escritura'

# ================================================================================
# ARCHIVO 5/5: superficie_insuficiente_exception.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ================================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """Se lanza cuando no hay suficiente superficie disponible para plantar."""
    def __init__(self, user_message: str, superficie_requerida: float, superficie_disponible: float):
        super().__init__(user_message)
        self.superficie_requerida = superficie_requerida
        self.superficie_disponible = superficie_disponible


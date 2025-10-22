from python_forestacion.excepciones.forestacion_exception import ForestacionException

class PersistenciaException(ForestacionException):
    """Se lanza cuando ocurre un error al leer o escribir archivos de persistencia."""
    def __init__(self, user_message: str, ruta_archivo: str, operacion: str):
        super().__init__(user_message)
        self.ruta_archivo = ruta_archivo
        self.operacion = operacion # 'lectura' o 'escritura'
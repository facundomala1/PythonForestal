from python_forestacion.excepciones.forestacion_exception import ForestacionException

class AguaAgotadaException(ForestacionException):
    """Se lanza cuando no hay suficiente agua en la plantación para una operación."""
    def __init__(self, user_message: str, agua_requerida: int, agua_disponible: int):
        super().__init__(user_message)
        self.agua_requerida = agua_requerida
        self.agua_disponible = agua_disponible
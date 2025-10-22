from python_forestacion.excepciones.forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """Se lanza cuando no hay suficiente superficie disponible para plantar."""
    def __init__(self, user_message: str, superficie_requerida: float, superficie_disponible: float):
        super().__init__(user_message)
        self.superficie_requerida = superficie_requerida
        self.superficie_disponible = superficie_disponible
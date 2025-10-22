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
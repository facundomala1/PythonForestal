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
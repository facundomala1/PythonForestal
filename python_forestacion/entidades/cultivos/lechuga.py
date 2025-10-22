from python_forestacion.entidades.cultivos.hortaliza import Hortaliza

# Valores que luego irán en constantes.py
SUPERFICIE_LECHUGA = 0.10
AGUA_INICIAL_LECHUGA = 1

class Lechuga(Hortaliza):
    """
    Entidad Lechuga. Hereda de Hortaliza y representa un cultivo de lechuga.
    """
    def __init__(self, variedad: str):
        """
        Args:
            variedad (str): La variedad de la lechuga (ej. "Crespa", "Mantecosa").
        """
        super().__init__(
            superficie=SUPERFICIE_LECHUGA,
            agua=AGUA_INICIAL_LECHUGA,
            invernadero=True  # Las lechugas siempre van en invernadero
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad

    def __str__(self) -> str:
        return (f"Cultivo: Lechuga (ID: {self.get_id()})\n"
                f"  - Variedad: {self.get_variedad()}\n"
                f"  - Invernadero: {'Sí' if self.necesita_invernadero() else 'No'}\n"
                f"  - Agua: {self.get_agua()} L\n"
                f"  - Superficie: {self.get_superficie()} m²")
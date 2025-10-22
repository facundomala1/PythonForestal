from python_forestacion.entidades.cultivos.hortaliza import Hortaliza

# Valores que luego irán en constantes.py
SUPERFICIE_ZANAHORIA = 0.15
AGUA_INICIAL_ZANAHORIA = 0

class Zanahoria(Hortaliza):
    """
    Entidad Zanahoria. Hereda de Hortaliza y representa un cultivo de zanahoria.
    """
    def __init__(self, es_baby: bool):
        """
        Args:
            es_baby (bool): True si es una baby carrot, False si es regular.
        """
        super().__init__(
            superficie=SUPERFICIE_ZANAHORIA,
            agua=AGUA_INICIAL_ZANAHORIA,
            invernadero=False  # Las zanahorias no requieren invernadero
        )
        self._es_baby_carrot = es_baby

    def es_baby_carrot(self) -> bool:
        return self._es_baby_carrot

    def __str__(self) -> str:
        return (f"Cultivo: Zanahoria (ID: {self.get_id()})\n"
                f"  - Tipo: {'Baby Carrot' if self.es_baby_carrot() else 'Regular'}\n"
                f"  - Invernadero: {'Sí' if self.necesita_invernadero() else 'No'}\n"
                f"  - Agua: {self.get_agua()} L\n"
                f"  - Superficie: {self.get_superficie()} m²")
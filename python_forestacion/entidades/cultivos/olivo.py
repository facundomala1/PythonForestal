from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna

# Valores que luego irán en constantes.py
SUPERFICIE_OLIVO = 3.0
AGUA_INICIAL_OLIVO = 5
ALTURA_INICIAL_OLIVO = 0.5

class Olivo(Arbol):
    """
    Entidad Olivo. Hereda de Arbol y representa un cultivo de olivo.
    """
    def __init__(self, tipo_aceituna: TipoAceituna):
        """
        Args:
            tipo_aceituna (TipoAceituna): El tipo de aceituna del olivo.
        """
        super().__init__(
            superficie=SUPERFICIE_OLIVO,
            agua=AGUA_INICIAL_OLIVO,
            altura=ALTURA_INICIAL_OLIVO
        )
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        return self._tipo_aceituna

    def set_tipo_aceituna(self, tipo_aceituna: TipoAceituna) -> None:
        self._tipo_aceituna = tipo_aceituna

    def __str__(self) -> str:
        return (f"Cultivo: Olivo (ID: {self.get_id()})\n"
                f"  - Tipo Aceituna: {self.get_tipo_aceituna().name}\n"
                f"  - Altura: {self.get_altura():.2f} m\n"
                f"  - Agua: {self.get_agua()} L\n"
                f"  - Superficie: {self.get_superficie()} m²")
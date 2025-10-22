from enum import Enum, auto

class TipoAceituna(Enum):
    """
    Enumeración para los tipos de aceituna que puede tener un Olivo.
    """
    ARBEQUINA = auto()
    PICUAL = auto()
    MANZANILLA = auto()
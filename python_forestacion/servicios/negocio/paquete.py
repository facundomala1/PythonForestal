from typing import List, TypeVar, Generic, Type

# T es una variable de tipo genérica. Puede representar cualquier clase.
T = TypeVar('T')

class Paquete(Generic[T]):
    """
    Una clase genérica que representa un paquete o caja de un tipo específico de cultivo.
    Utiliza Generics para garantizar la seguridad de tipos.
    """
    _id_counter = 0

    def __init__(self, tipo_contenido: Type[T]):
        """
        Args:
            tipo_contenido (Type[T]): El tipo de clase que contendrá el paquete.
        """
        Paquete._id_counter += 1
        self._id_paquete = Paquete._id_counter
        self._tipo_contenido = tipo_contenido
        self._contenido: List[T] = []

    def agregar_item(self, item: T) -> None:
        """Agrega un item al paquete, verificando que sea del tipo correcto."""
        if not isinstance(item, self._tipo_contenido):
            raise TypeError(f"Este paquete solo acepta {self._tipo_contenido.__name__}")
        self._contenido.append(item)

    def agregar_items(self, items: List[T]) -> None:
        """Agrega una lista de items al paquete."""
        for item in items:
            self.agregar_item(item)

    def mostrar_contenido_caja(self) -> None:
        """Muestra un resumen del contenido del paquete."""
        print("\n--- Contenido de la Caja ---")
        print(f"  ID Paquete: {self._id_paquete}")
        print(f"  Tipo:       {self._tipo_contenido.__name__}")
        print(f"  Cantidad:   {len(self._contenido)} unidades")
        print("----------------------------")
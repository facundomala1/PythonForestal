from typing import TYPE_CHECKING, Dict, Callable

# Para evitar importaciones circulares y mantener el código limpio
if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.cultivos.pino import Pino
    from python_forestacion.entidades.cultivos.olivo import Olivo
    from python_forestacion.entidades.cultivos.lechuga import Lechuga
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
    from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna

class CultivoFactory:
    """
    Patrón Factory Method para la creación de diferentes tipos de cultivos.
    Encapsula la lógica de instanciación para desacoplar el cliente de las clases concretas.
    """

    @staticmethod
    def _crear_pino() -> 'Pino':
        from python_forestacion.entidades.cultivos.pino import Pino
        # Por simplicidad, asignamos una variedad por defecto.
        return Pino(variedad="Parana")

    @staticmethod
    def _crear_olivo() -> 'Olivo':
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
        # Asignamos un tipo de aceituna por defecto.
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)

    @staticmethod
    def _crear_lechuga() -> 'Lechuga':
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        return Lechuga(variedad="Mantecosa")

    @staticmethod
    def _crear_zanahoria() -> 'Zanahoria':
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        # Creamos zanahorias regulares por defecto.
        return Zanahoria(es_baby=False)

    @staticmethod
    def crear_cultivo(especie: str) -> 'Cultivo':
        """
        El método fábrica principal.
        
        Args:
            especie (str): El nombre del tipo de cultivo a crear (ej. "Pino").

        Returns:
            Cultivo: Una instancia del cultivo solicitado.

        Raises:
            ValueError: Si la especie no es conocida por la fábrica.
        """
        # Usamos un diccionario para mapear nombres a funciones de creación.
        # Esto es más extensible que un if/elif/else.
        factories: Dict[str, Callable[[], 'Cultivo']] = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(f"Especie de cultivo desconocida: {especie}")

        # Llama a la función de creación correcta y devuelve el objeto.
        return factories[especie]()
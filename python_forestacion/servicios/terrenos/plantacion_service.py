from typing import TYPE_CHECKING
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion

# Valores que luego irán a constantes.py
AGUA_RIEGO = 10
CRECIMIENTO_PINO = 0.10
CRECIMIENTO_OLIVO = 0.01

class PlantacionService:
    """
    Servicio con la lógica de negocio para las operaciones de una Plantacion.
    """
    def __init__(self):
        self._registry = CultivoServiceRegistry.get_instance()

    def plantar(self, plantacion: 'Plantacion', especie: str, cantidad: int) -> None:
        """
        Planta una cantidad de cultivos de una especie en la plantación.
        Utiliza el Patrón Factory para crear los cultivos.
        """
        # 1. Crear un cultivo temporal para saber cuánta superficie necesita
        cultivo_temporal = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_temporal.get_superficie() * cantidad

        # 2. Validar que haya superficie disponible
        if plantacion.get_superficie_disponible() < superficie_requerida:
            # Más adelante crearemos excepciones personalizadas
            raise ValueError("Superficie insuficiente para plantar.")

        # 3. Crear y agregar los cultivos
        for _ in range(cantidad):
            nuevo_cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.agregar_cultivo(nuevo_cultivo)
        
        print(f"Se plantaron {cantidad} unidades de {especie}.")

    def regar(self, plantacion: 'Plantacion') -> None:
        """
        Riega todos los cultivos de la plantación.
        Utiliza el Registry para delegar la absorción de agua.
        """
        # 1. Validar y consumir agua de la plantación
        if plantacion.get_agua_disponible() < AGUA_RIEGO:
            raise ValueError("Agua insuficiente en la plantación para regar.")
        
        plantacion.set_agua_disponible(plantacion.get_agua_disponible() - AGUA_RIEGO)
        
        # 2. Cada cultivo absorbe agua según su estrategia
        for cultivo in plantacion.get_cultivos():
            agua_absorbida = self._registry.absorver_agua(cultivo)
            print(f"El cultivo {cultivo.get_id()} ({type(cultivo).__name__}) absorbió {agua_absorbida}L de agua.")
            
            # Lógica de crecimiento específica
            from python_forestacion.entidades.cultivos.pino import Pino
            from python_forestacion.entidades.cultivos.olivo import Olivo
            if isinstance(cultivo, Pino):
                pino_service = self._registry.get_servicio(cultivo)
                pino_service.crecer(cultivo, CRECIMIENTO_PINO)
            elif isinstance(cultivo, Olivo):
                olivo_service = self._registry.get_servicio(cultivo)
                olivo_service.crecer(cultivo, CRECIMIENTO_OLIVO)

    def fumigar(self, plantacion: 'Plantacion', plaguicida: str) -> None:
        """Fumiga toda la plantación."""
        print(f"Fumigando la plantación '{plantacion.get_nombre()}' con {plaguicida}.")

    def mostrar_cultivos(self, plantacion: 'Plantacion') -> None:
        """Muestra los datos de todos los cultivos en la plantación."""
        print("\n--- Listado de Cultivos en la Plantación ---")
        for cultivo in plantacion.get_cultivos():
            self._registry.mostrar_datos(cultivo)
            print("-" * 20)
"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/riego/control
Fecha: 2025-10-21 23:16:16
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/riego/control/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: control_riego_task.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/riego/control/control_riego_task.py
# ================================================================================

import threading
import time
from typing import TYPE_CHECKING
from python_forestacion.patrones.observer.observer import Observer

if TYPE_CHECKING:
    from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
    from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
    from python_forestacion.entidades.terrenos.plantacion import Plantacion

# Valores que luego irán a constantes.py
TEMP_MIN_RIEGO = 8.0
TEMP_MAX_RIEGO = 15.0
HUMEDAD_MAX_RIEGO = 50.0
INTERVALO_CONTROL_RIEGO = 2.5  # segundos

class ControlRiegoTask(threading.Thread, Observer[float]):
    """
    Controlador que se ejecuta en un hilo y observa los sensores para decidir
    cuándo regar la plantación. Es un Observer.
    """
    def __init__(
        self,
        sensor_temperatura: 'TemperaturaReaderTask',
        sensor_humedad: 'HumedadReaderTask',
        plantacion: 'Plantacion',
        plantacion_service: 'PlantacionService'
    ):
        threading.Thread.__init__(self, daemon=True)
        # Nota: No llamamos a super() de Observer porque no tiene __init__

        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        self._detenido = threading.Event()

        # Guardamos los últimos valores conocidos de los sensores
        self._ultima_temperatura: float = 20.0  # Valor inicial seguro
        self._ultima_humedad: float = 60.0    # Valor inicial seguro
        
        # Suscribirse a ambos sensores
        sensor_temperatura.agregar_observador(self)
        sensor_humedad.agregar_observador(self)

    def actualizar(self, evento: float) -> None:
        """
        Este método es llamado por CUALQUIER sensor (Observable).
        Aquí, inferimos si el dato es temperatura o humedad por su rango.
        Esta es una simplificación; un sistema real usaría un evento más complejo.
        """
        # Heurística para diferenciar el origen del dato
        from python_forestacion.riego.sensores.temperatura_reader_task import SENSOR_TEMP_MIN, SENSOR_TEMP_MAX
        if SENSOR_TEMP_MIN <= evento <= SENSOR_TEMP_MAX:
            self._ultima_temperatura = evento
        else: # Asumimos que es humedad si no encaja en el rango de temperatura
            self._ultima_humedad = evento

    def _evaluar_condiciones_riego(self):
        """Evalúa si se debe regar basado en los últimos datos de los sensores."""
        temp = self._ultima_temperatura
        hum = self._ultima_humedad

        print(f"[Control Riego]: Evaluando... Temp={temp}°C, Humedad={hum}%")

        if (TEMP_MIN_RIEGO <= temp <= TEMP_MAX_RIEGO) and (hum < HUMEDAD_MAX_RIEGO):
            print(f"[Control Riego]: CONDICIONES ÓPTIMAS. Iniciando riego...")
            try:
                self._plantacion_service.regar(self._plantacion)
                print("[Control Riego]: Riego completado exitosamente.")
            except ValueError as e:
                print(f"[Control Riego]: ERROR AL REGAR - {e}")
        else:
            print("[Control Riego]: Condiciones no aptas para riego. Esperando...")

    def run(self):
        """El código del hilo del controlador."""
        print("Control de Riego: INICIADO")
        while not self._detenido.is_set():
            self._evaluar_condiciones_riego()
            time.sleep(INTERVALO_CONTROL_RIEGO)
        print("Control de Riego: DETENIDO")

    def detener(self):
        """Señaliza al hilo que debe detenerse."""
        self._detenido.set()


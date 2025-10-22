"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/riego/sensores
Fecha: 2025-10-21 23:16:16
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/riego/sensores/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: humedad_reader_task.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/riego/sensores/humedad_reader_task.py
# ================================================================================

import random
import time
import threading
from python_forestacion.patrones.observer.observable import Observable

# Valores que luego irán a constantes.py
INTERVALO_SENSOR_HUMEDAD = 3.0  # segundos
SENSOR_HUMEDAD_MIN = 0.0
SENSOR_HUMEDAD_MAX = 100.0

class HumedadReaderTask(threading.Thread, Observable[float]):
    """
    Un sensor que lee la humedad en un hilo separado.
    Actúa como un Observable, notificando a sus observadores de cada nueva lectura.
    """
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _leer_humedad(self) -> float:
        """Simula la lectura de un sensor de humedad."""
        return round(random.uniform(SENSOR_HUMEDAD_MIN, SENSOR_HUMEDAD_MAX), 2)

    def run(self):
        """El código que se ejecuta cuando el hilo comienza."""
        print("Sensor de Humedad: INICIADO")
        while not self._detenido.is_set():
            humedad = self._leer_humedad()
            print(f"[Sensor Humedad]: Nueva lectura -> {humedad}%")
            self.notificar_observadores(humedad)
            time.sleep(INTERVALO_SENSOR_HUMEDAD)
        print("Sensor de Humedad: DETENIDO")

    def detener(self):
        """Señaliza al hilo que debe detenerse."""
        self._detenido.set()

# ================================================================================
# ARCHIVO 3/3: temperatura_reader_task.py
# Ruta: /home/facundo/Documentos/DiseñoSistema/PythonForestal/python_forestacion/riego/sensores/temperatura_reader_task.py
# ================================================================================

import random
import time
import threading
from python_forestacion.patrones.observer.observable import Observable

# Valores que luego irán a constantes.py
INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
SENSOR_TEMP_MIN = -25.0
SENSOR_TEMP_MAX = 50.0

class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """
    Un sensor que lee la temperatura en un hilo separado.
    Actúa como un Observable, notificando a sus observadores de cada nueva lectura.
    """
    def __init__(self):
        # Es crucial llamar a los constructores de ambas clases padre
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _leer_temperatura(self) -> float:
        """Simula la lectura de un sensor de temperatura."""
        return round(random.uniform(SENSOR_TEMP_MIN, SENSOR_TEMP_MAX), 2)

    def run(self):
        """El código que se ejecuta cuando el hilo comienza (con .start())."""
        print("Sensor de Temperatura: INICIADO")
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            print(f"[Sensor Temp]: Nueva lectura -> {temperatura}°C")
            self.notificar_observadores(temperatura)
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)
        print("Sensor de Temperatura: DETENIDO")

    def detener(self):
        """Señaliza al hilo que debe detenerse de forma segura."""
        self._detenido.set()


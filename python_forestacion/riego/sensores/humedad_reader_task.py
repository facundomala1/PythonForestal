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
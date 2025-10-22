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
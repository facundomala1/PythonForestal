import time
from datetime import date

# Importaciones de Entidades
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal

# Importaciones de Servicios
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.negocio.fincas_service import FincasService

# Importaciones del Sistema de Riego (Threads)
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

# Importaciones de Excepciones y Constantes
from python_forestacion.constantes import THREAD_JOIN_TIMEOUT
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException


def run_simulation():
    """Función principal que ejecuta toda la simulación del sistema."""

    print("======================================================================")
    print("         SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
    print("======================================================================")

    # --- 1. Creación de la Finca y Plantación ---
    print("\n[PASO 1]: Creando la finca y la plantación...")
    tierra_service = TierraService()
    terreno = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=10000.0,
        domicilio="Agrelo, Mendoza",
        nombre_plantacion="Finca del Madero"
    )
    plantacion = terreno.get_finca()
    print(f"Finca '{plantacion.get_nombre()}' creada con {terreno.get_superficie()} m² disponibles.")

    # --- 2. Plantación de Cultivos (Uso de Factory Method) ---
    print("\n[PASO 2]: Plantando diversos cultivos...")
    plantacion_service = PlantacionService()
    try:
        plantacion_service.plantar(plantacion, "Pino", 5)
        plantacion_service.plantar(plantacion, "Olivo", 5)
        plantacion_service.plantar(plantacion, "Lechuga", 5)
        plantacion_service.plantar(plantacion, "Zanahoria", 5)
    except SuperficieInsuficienteException as e:
        print(f"ERROR: {e.get_full_message()}")
    
    print(f"Superficie disponible restante: {plantacion.get_superficie_disponible():.2f} m².")

    # --- 3. Gestión de Personal y Tareas ---
    print("\n[PASO 3]: Contratando personal y asignando tareas...")
    trabajador_service = TrabajadorService()
    tareas = [
        Tarea(1, date.today(), "Desmalezar sector norte"),
        Tarea(2, date.today(), "Abonar pinos"),
        Tarea(3, date.today(), "Revisar sistema de riego")
    ]
    # Aquí iría la lógica para crear un trabajador y asignarle las tareas
    # Por simplicidad, lo haremos directamente en el servicio.

    # --- 4. Sistema de Riego Automatizado (Uso de Observer y Threads) ---
    print("\n[PASO 4]: Activando el sistema de riego automatizado...")
    tarea_temp = TemperaturaReaderTask()
    tarea_hum = HumedadReaderTask()
    tarea_control = ControlRiegoTask(
        sensor_temperatura=tarea_temp,
        sensor_humedad=tarea_hum,
        plantacion=plantacion,
        plantacion_service=plantacion_service
    )
    
    # Iniciamos los hilos
    tarea_temp.start()
    tarea_hum.start()
    tarea_control.start()

    print("Sistema de riego funcionando en segundo plano durante 10 segundos...")
    time.sleep(10)

    # Detenemos los hilos de forma segura
    print("\nDeteniendo el sistema de riego...")
    tarea_temp.detener()
    tarea_hum.detener()
    tarea_control.detener()

    tarea_temp.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_hum.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_control.join(timeout=THREAD_JOIN_TIMEOUT)
    print("Sistema de riego detenido de forma segura.")

    # --- 5. Operaciones de Negocio (Cosecha y Fumigación) ---
    print("\n[PASO 5]: Realizando operaciones de negocio...")
    fincas_service = FincasService()
    # (El registro se crea más abajo)
    
    # --- 6. Persistencia de Datos ---
    print("\n[PASO 6]: Creando y guardando el registro forestal...")
    registro_forestal = RegistroForestal(
        id_padron=1,
        tierra=terreno,
        plantacion=plantacion,
        propietario="Juan Perez",
        avaluo=50309233.55
    )
    
    registro_service = RegistroForestalService()
    registro_service.persistir(registro_forestal)

    # --- 7. Recuperación y Verificación ---
    print("\n[PASO 7]: Leyendo el registro desde el disco para verificación...")
    registro_leido = RegistroForestalService.leer_registro("Juan Perez")
    
    # Mostramos el reporte final con los datos leídos
    registro_service.mostrar_datos(registro_leido)

    print("\n======================================================================")
    print("              EJEMPLO COMPLETADO EXITOSAMENTE")
    print("======================================================================")

if __name__ == "__main__":
    run_simulation()
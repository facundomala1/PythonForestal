# ==============================================================================
# CONSTANTES DEL SISTEMA DE GESTION FORESTAL
# ==============================================================================

# ------------------------------------------------------------------------------
# Archivos y Persistencia
# ------------------------------------------------------------------------------
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"
THREAD_JOIN_TIMEOUT = 2.0  # segundos

# ------------------------------------------------------------------------------
# Terrenos y Plantaciones
# ------------------------------------------------------------------------------
AGUA_INICIAL_PLANTACION = 500  # litros
AGUA_RIEGO = 10                # litros consumidos por riego

# ------------------------------------------------------------------------------
# Cultivos: Pino
# ------------------------------------------------------------------------------
SUPERFICIE_PINO = 2.0          # m²
AGUA_INICIAL_PINO = 2          # litros
ALTURA_INICIAL_ARBOL = 1.0     # metros (usado por Pino)
CRECIMIENTO_PINO = 0.10        # metros por riego

# ------------------------------------------------------------------------------
# Cultivos: Olivo
# ------------------------------------------------------------------------------
SUPERFICIE_OLIVO = 3.0         # m²
AGUA_INICIAL_OLIVO = 5         # litros
ALTURA_INICIAL_OLIVO = 0.5     # metros
CRECIMIENTO_OLIVO = 0.01       # metros por riego

# ------------------------------------------------------------------------------
# Cultivos: Lechuga
# ------------------------------------------------------------------------------
SUPERFICIE_LECHUGA = 0.10      # m²
AGUA_INICIAL_LECHUGA = 1       # litros
ABSORCION_LECHUGA = 1          # litros

# ------------------------------------------------------------------------------
# Cultivos: Zanahoria
# ------------------------------------------------------------------------------
SUPERFICIE_ZANAHORIA = 0.15    # m²
AGUA_INICIAL_ZANAHORIA = 0     # litros
ABSORCION_ZANAHORIA = 2        # litros

# ------------------------------------------------------------------------------
# Sistema de Riego Automatizado
# ------------------------------------------------------------------------------
INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
SENSOR_TEMP_MIN = -25.0             # °C
SENSOR_TEMP_MAX = 50.0              # °C

INTERVALO_SENSOR_HUMEDAD = 3.0      # segundos
SENSOR_HUMEDAD_MIN = 0.0            # %
SENSOR_HUMEDAD_MAX = 100.0          # %

INTERVALO_CONTROL_RIEGO = 2.5       # segundos
TEMP_MIN_RIEGO = 8.0                # °C
TEMP_MAX_RIEGO = 15.0               # °C
HUMEDAD_MAX_RIEGO = 50.0            # %

# ------------------------------------------------------------------------------
# Estrategias de Absorción de Agua
# ------------------------------------------------------------------------------
MES_INICIO_VERANO = 3               # Marzo
MES_FIN_VERANO = 8                  # Agosto
ABSORCION_SEASONAL_VERANO = 5       # litros
ABSORCION_SEASONAL_INVIERNO = 2     # litros
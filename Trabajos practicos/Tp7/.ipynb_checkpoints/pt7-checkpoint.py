import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones para calcular el esfuerzo y el tiempo de desarrollo
def calcular_esfuerzo(S):
    return 8 * S ** 0.95

def calcular_tiempo_desarrollo(E):
    return 2.4 * E ** 0.33

# Generar los datos para el intervalo de tamaños [0, 10000] y esfuerzos [1, 500]
tamanos = np.linspace(0, 10000, 1000)
esfuerzos = np.linspace(1, 500, 1000)

# Calcular esfuerzo para cada tamaño
esfuerzo_valores = calcular_esfuerzo(tamanos)

# Calcular tiempo de desarrollo para cada esfuerzo
tiempo_desarrollo_valores = calcular_tiempo_desarrollo(esfuerzos)

# Crear la gráfica del esfuerzo en función del tamaño del proyecto
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(tamanos, esfuerzo_valores, color='blue')
plt.title('Esfuerzo vs Tamaño del Proyecto')
plt.xlabel('Tamaño del Proyecto (KLOC)')
plt.ylabel('Esfuerzo (persona-meses)')
plt.grid(True)

# Crear la gráfica del tiempo de desarrollo en función del esfuerzo
plt.subplot(1, 2, 2)
plt.plot(esfuerzos, tiempo_desarrollo_valores, color='green')
plt.title('Tiempo de Desarrollo vs Esfuerzo')
plt.xlabel('Esfuerzo (persona-meses)')
plt.ylabel('Tiempo de Desarrollo (meses)')
plt.grid(True)

# Mostrar las gráficas
plt.tight_layout()
plt.show()

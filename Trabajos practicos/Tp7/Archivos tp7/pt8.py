import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.integrate import quad
import argparse

# Definición de la función del esfuerzo instantáneo
def esfuerzo_instantaneo(t, K, a):
    return 2 * K * a * t * np.exp(-a * t**2)

# Función para calcular el esfuerzo acumulado en función del tiempo
def esfuerzo_acumulado(t, K, a):
    return K * (1 - np.exp(-a * t**2))

# Calcular la media del staff en un intervalo de tiempo
def average_value(K, a, tx):
    integral, _ = quad(esfuerzo_instantaneo, 0, tx, args=(K, a))
    return integral / tx

# Datos históricos de calibración
t_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])        # Tiempo en meses
E_data = np.array([8, 21, 25, 30, 25, 24, 17, 15, 11, 6])  # Esfuerzo instantáneo en persona-mes

# Crear el dataset en pandas
df = pd.DataFrame({'Tiempo (meses)': t_data, 'Esfuerzo (PM)': E_data})
print(df)

# Estimar el valor de K a partir de los datos históricos
K_est = np.sum(E_data)
print(f"Esfuerzo total estimado (K) basado en datos históricos: {K_est} PM")

# Calibrar el modelo para estimar el parámetro 'a' usando curve_fit
popt, _ = curve_fit(lambda t, a: esfuerzo_instantaneo(t, K_est, a), t_data, E_data, p0=[0.1])
a_estimada = popt[0]
print(f"Parámetro 'a' estimado a partir de los datos: {a_estimada:.3f}")

# Gráfica de los datos históricos y el modelo ajustado
t_fit = np.linspace(min(t_data), max(t_data), 100)
E_fit = esfuerzo_instantaneo(t_fit, K_est, a_estimada)

plt.scatter(t_data, E_data, label='Datos históricos', color='blue')
plt.plot(t_fit, E_fit, label='Modelo ajustado', color='red')
plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo instantáneo (PM)')
plt.legend()
plt.show()

# Recibir el esfuerzo del proyecto como parámetro de entrada
ap = argparse.ArgumentParser()
ap.add_argument("-k", "--esfuerzo", required=True, help="Esfuerzo total del proyecto en PM", type=float)
args = vars(ap.parse_args())

K_proyecto = args['esfuerzo']
print(f"Esfuerzo del proyecto ingresado: {K_proyecto} PM")

# Graficar el modelo PNR para el esfuerzo del proyecto ingresado
E_proyecto_fit = esfuerzo_instantaneo(t_fit, K_proyecto, a_estimada)

plt.plot(t_fit, E_proyecto_fit, label=f'Proyecto (K={K_proyecto} PM)', color='green')
plt.plot(t_fit, E_fit, label='Modelo ajustado (histórico)', color='red')
plt.scatter(t_data, E_data, label='Datos históricos', color='blue')
plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo instantáneo (PM)')
plt.legend()
plt.show()

# Calcular el valor medio del staff requerido durante el proyecto
t_proyecto = max(t_fit)
pmed_proyecto = average_value(K_proyecto, a_estimada, t_proyecto)
print(f"Staff promedio requerido para el proyecto: {pmed_proyecto:.2f} personas")

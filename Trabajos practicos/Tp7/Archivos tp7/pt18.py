import numpy as np

# Parámetros
inversion_mensual = 1000
n_meses = 15
tasa_mensual = 0.01
valor_flujos_futuros = 18000

# Cálculo del valor presente de la inversión
VP_inversion = inversion_mensual * (1 - (1 + tasa_mensual)**-n_meses) / tasa_mensual

# Cálculo del valor presente de los flujos futuros
VP_flujos = valor_flujos_futuros / (1 + tasa_mensual)**n_meses

# Cálculo del VPN
VPN = VP_flujos - VP_inversion

print(f"Valor presente de la inversión: ${VP_inversion:.2f}")
print(f"Valor presente de los flujos futuros: ${VP_flujos:.2f}")
print(f"Valor presente neto (VPN): ${VPN:.2f}")

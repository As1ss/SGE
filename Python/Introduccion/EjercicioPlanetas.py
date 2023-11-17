from scipy.constants import G
from numpy.matlib import sqrt


r=6371e3
M = 5.972e24



print()

datos_planetas = {
    'Mercurio': {'masa': 3.3011e23, 'radio': 2.4397e6},
    'Venus': {'masa': 4.8675e24, 'radio': 6.0518e6},
    'Tierra': {'masa': 5.972e24, 'radio': 6.371e6},
    'Marte': {'masa': 6.4171e23, 'radio': 3.3895e6},
    'Júpiter': {'masa': 1.8982e27, 'radio': 6.9911e7},
    'Saturno': {'masa': 5.6834e26, 'radio': 5.8232e7},
    'Urano': {'masa': 8.6810e25, 'radio': 2.5362e7},
    'Neptuno': {'masa': 1.0243e26, 'radio': 2.4622e7},
    'Plutón': {'masa': 1.303e22, 'radio': 1.1883e6}
}

# Imprimir los nombres de los planetas, su masa y su radio
for nombre in datos_planetas:
    masa = datos_planetas[nombre]["masa"]
    radio = datos_planetas[nombre]["radio"]
    ve = sqrt((2*G*masa)/radio)
    print()
    print(f'Planeta: {nombre}')
    print(f'Masa: {datos_planetas[nombre]["masa"]}')
    print(f'Radio: {datos_planetas[nombre]["radio"]}')
    print(f'Velocidad de escape: {round(ve/1000,3)}')
    datos_planetas[nombre]["v_escape"]= round(ve/1000,3)
    print()
   
for nombre in datos_planetas:
    print()
    print(f"Planteta: {nombre}")
    print(f"Masa: {datos_planetas[nombre]['masa']}")
    print(f"Radio: {datos_planetas[nombre]['radio']}")
    print(f"Velocidad escape: {datos_planetas[nombre]['v_escape']}")
    print()

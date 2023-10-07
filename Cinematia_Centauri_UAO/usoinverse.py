
#INCOMPLETO

import numpy as np
from inversekinematic4 import inversekinematic4

# Matriz de transformación que representa la posición y orientación de la mano del manipulador
#A partir de la matriz T obtengo los valores de las articulaciones
""" T = np.array([[ 0, 0, 1, 0.3],
              [-1, 0, 0, 0],
              [ 0, 1, 0, 0.5],
              [ 0, 0, 0, 1]]) """
T = np.array([[ 1.00000000e+00 , 1.22464680e-16 , 7.49879891e-33 , 1.72000000e-01],
 [-1.22464680e-16 , 1.00000000e+00 , 1.22464680e-16 , 7.43360607e-18],
 [ 0.00000000e+00 , -1.22464680e-16 , 1.00000000e+00 , 4.11200000e-01],
 [ 0.00000000e+00 , 0.00000000e+00 , 0.00000000e+00 , 1.00000000e+00]])
q = [0, np.pi/2, 0, 0,np.pi/2,0]

teta = np.array([q[0], q[1], q[2], q[3],q[4],q[5]])
d = np.array([0.223, 0, 0, 0.172, 0,0.1052])
a = np.array([0, 0.083, 0, 0, 0, 0])
alfa = np.array([np.pi/2, 0, np.pi/2, np.pi/2, np.pi/2, 0])
# Calcular el vector de coordenadas articulares correspondiente a la solución cinemática inversa
q = inversekinematic4(T,teta,d,a,alfa)

# Imprimir el vector de coordenadas articulares
print(q)

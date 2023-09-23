import numpy as np
from inversekinematic4 import inversekinematic4

# Matriz de transformación que representa la posición y orientación de la mano del manipulador
""" T = np.array([[ 0, 0, 1, 0.3],
              [-1, 0, 0, 0],
              [ 0, 1, 0, 0.5],
              [ 0, 0, 0, 1]]) """
T = np.array([[ 6.28293770e-01, -1.16247610e-02, -7.77889326e-01, -5.73524473e-01],
 [ 7.77756214e-01 ,-1.43901317e-02, 6.28401302e-01 , 3.34756522e-01],
 [-1.84989447e-02 ,-9.99828880e-01 , 6.12323400e-17 , 1.16210000e+00],
 [ 0.00000000e+00 , 0.00000000e+00 , 0.00000000e+00 , 1.00000000e+00]])
q=[0,0,0,0]
teta = np.array([q[0], 0, 0, q[3]])
d = np.array([0.4, q[1], q[2], 0.2])
a = np.array([0, -0.1, 0, 0])
alfa = np.array([0, -np.pi/2, 0, 0])
# Calcular el vector de coordenadas articulares correspondiente a la solución cinemática inversa
q = inversekinematic4(T,teta,d,a,alfa)

# Imprimir el vector de coordenadas articulares
print(q)

import numpy as np
from directkinematic4 import directkinematic4

# Ejemplo de uso
q = np.array([00.8913, 0.7621, 0.4565, 0.0185])
teta = np.array([q[0], 0, 0, q[3]])
d = np.array([0.4, q[1], q[2], 0.2])
a = np.array([0, -0.1, 0, 0])
alfa = np.array([0, -np.pi/2, 0, 0])
A04 = directkinematic4(teta, d, a, alfa)

# Imprimir la matriz de transformación homogénea
print(A04)

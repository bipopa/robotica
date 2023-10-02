from inversekinematic import cinematica_inversa_centauri
from matriz_rotacion import matriz_rotacion
import numpy as np
l0 = 0.17                              # Longitud eslabón 1
l1 = 0.22                               # Longitud eslabón 2
l2 = 0.22                               # Longitud eslabón 3 
l3 = 0.1
Tdes = np.identity(4)  # Matriz de identidad 4x4
Tdes[:3, 3] = np.array([-0.16, -0.16, 0.620])
print (Tdes,"tdes2")
#ejemplo de uso cinematica inversa
z=cinematica_inversa_centauri(Tdes,l0,l1,l2,l3)
print(z)

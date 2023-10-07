from inversekinematic import cinematica_inversa_centaurirad, cinematica_inversa_centauri
from matriz_rotacion import matriz_rotacion
import numpy as np
l0 = 0.17                              # Longitud eslabón 1
l1 = 0.22                               # Longitud eslabón 2
l2 = 0.22                               # Longitud eslabón 3 
l3 = 0.1
Tdes = np.identity(4)  # Matriz de identidad 4x4
n=[0.05999119, 0.02659445, -0.99784457]
s=[-0.05663413, -0.99794411, -0.03000199 ]   
a=[-0.99659101, 0.05831192, -0.0583617]
p=[0, 0 ,0]
Tr = np.array([n, s, a, p]).T
Tdes[:3, 3] = np.array([-0.4,-0.05,0.4])
p1=[-0.4,-0.05,0.4] 
p2=[-0.4, -0.05, 0]
p3=[-0.2, -0.05 ,0]
p4=[-0.2, -0.05, 0.01]
p5=[-0.2, -0.05 ,0.4]
print (Tdes,"tdes2")
#ejemplo de uso cinematica inversa
z=cinematica_inversa_centaurirad(Tr,l0,l1,l2,l3)
print(z)

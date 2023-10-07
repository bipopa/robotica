
#COMPLETO
#SIN ERRORES
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from drawrobot3d4 import drawrobot3d4
from inversekinematic import cinematica_inversa_centaurirad
import numpy as np
import time
# Llamar a la función drawrobot3d4 con valores de ejemplo
l0 = 0.170
l1 = 0.223
l2 = 0.223
l3 = 0.1052

p1=[-0.4,0.05,0.3] 
p2=[-0.4, 0.05, 0]
p3=[-0.2, 0.05 ,0]
p4=[-0.2, 0.05, 0.3]
#Orientación del robot, asegurese de cambiar estos parametros dependiendo del plano en el que desea dibujar
###########
n=[1,0,0] 
s=[0,1,0]
a=[0,0,1]
###########
Tr = np.array([n, s, a, p1]).T
q = cinematica_inversa_centaurirad(Tr,l0,l1,l2,l3)
print(q)

drawrobot3d4(q, l0, l1, l2,l3,1)

Tr = np.array([n, s, a, p2]).T
q = cinematica_inversa_centaurirad(Tr,l0,l1,l2,l3)
#q = [0, np.pi/2, 0, 0,np.pi/2,0]
print(q)

drawrobot3d4(q, l0, l1, l2,l3,1)

Tr = np.array([n, s, a, p3]).T
q = cinematica_inversa_centaurirad(Tr,l0,l1,l2,l3)
q = [0, np.pi/2, np.pi/2, 0,0,0]
print(q)

drawrobot3d4(q, l0, l1, l2,l3,1)




#COMPLETO
#SIN ERRORES

from drawrobot3d4 import drawrobot3d4
import numpy as np
# Llamar a la función drawrobot3d4 con valores de ejemplo
l0 = 0.223
l1 = 0.083
l2 = 0.172
l3 = 0.1052

q = [0, 0, 0, 0,0,0]

drawrobot3d4(q, l0, l1, l2,l3)


q = [0, np.pi/2, 0, 0,np.pi/2,0]

drawrobot3d4(q, l0, l1, l2,l3)

q = [0, np.pi/2, np.pi/2, 0,0,0]

drawrobot3d4(q, l0, l1, l2,l3)



q = [np.pi, 0, 0.3, 0]
drawrobot3d4(q, l0, l1, l2,l3)


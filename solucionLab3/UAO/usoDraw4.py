from drawrobot3d4 import drawrobot3d4
import numpy as np
from inversekinematic4 import inversekinematic4

# Llamar a la función drawrobot3d4 con valores de ejemplo

q = [1, 1, 0.3, 1]
teta = np.array([q[0], 0, 0, q[3]])
d = np.array([0.4, q[1], q[2], 0.2])
a = np.array([0, -0.1, 0, 0])
alfa = np.array([0, -np.pi/2, 0, 0])
drawrobot3d4(teta, d, a, alfa)

T = np.array([[ 2.91926582e-01, -4.54648713e-01, -8.41470985e-01, -4.74765723e-01],
 [ 4.54648713e-01, -7.08073418e-01,  5.40302306e-01,  1.86004054e-01],
 [-8.41470985e-01, -5.40302306e-01,  6.12323400e-17,  1.40000000e+00],
 [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  1.00000000e+00]]) 


q = [0,0,0,0]
teta = np.array([q[0], 0, 0, q[3]])
d = np.array([0.4, q[1], q[2], 0.2])
a = np.array([0, -0.1, 0, 0])
alfa = np.array([0, -np.pi/2, 0, 0])
q = inversekinematic4(T,teta,d,a,alfa)

drawrobot3d4(teta, d, a, alfa)

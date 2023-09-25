from drawrobot3d4 import drawrobot3d4
import numpy as np
# Llamar a la función drawrobot3d4 con valores de ejemplo
l0 = 0.223
l1 = 0.083
l2 = 0.172
l3 = 0.1052

q = [0, 0, 0, 0,0,0]

teta = np.array([q[0], q[1], q[2], q[3],q[4],q[5]])
d = np.array([l0, 0, 0, l2, 0,l3])
a = np.array([0, l1, 0, 0, 0, 0])
alfa = np.array([np.pi/2, 0, np.pi/2, np.pi/2, np.pi/2, 0])
drawrobot3d4(teta, d, a, alfa)


q = [0, np.pi/2, 0, 0,np.pi/2,0]

teta = np.array([q[0], q[1], q[2], q[3],q[4],q[5]])
d = np.array([l0, 0, 0, l2, 0,l3])
a = np.array([0, l1, 0, 0, 0, 0])
alfa = np.array([np.pi/2, 0, np.pi/2, np.pi/2, np.pi/2, 0])
drawrobot3d4(teta, d, a, alfa)

q = [0, np.pi/2, np.pi/2, 0,0,0]

teta = np.array([q[0], q[1], q[2], q[3],q[4],q[5]])
d = np.array([l0, 0, 0, l2, 0,l3])
a = np.array([0, l1, 0, 0, 0, 0])
alfa = np.array([np.pi/2, 0, np.pi/2, np.pi/2, np.pi/2, 0])
drawrobot3d4(teta, d, a, alfa)


""""""""""
q = [np.pi, 0, 0.3, 0]
teta = np.array([q[0], 0, 0, q[3]])
d = np.array([0.4, q[1], q[2], 0.2])
a = np.array([0, -0.1, 0, 0])
alfa = np.array([0, -np.pi/2, 0, 0])
drawrobot3d4(teta, d, a, alfa)"""
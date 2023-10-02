from drawrobot3d4 import drawrobot3d4
import numpy as np
# Llamar a la función drawrobot3d4 con valores de ejemplo

q = [1, 1, 0.3, 1]
teta = np.array([q[0], 0, 0, q[3]])
d = np.array([0.4, q[1], q[2], 0.2])
a = np.array([0, -0.1, 0, 0])
alfa = np.array([0, -np.pi/2, 0, 0])
drawrobot3d4(teta, d, a, alfa)

q = [np.pi, 0, 0.3, 0]
teta = np.array([q[0], 0, 0, q[3]])
d = np.array([0.4, q[1], q[2], 0.2])
a = np.array([0, -0.1, 0, 0])
alfa = np.array([0, -np.pi/2, 0, 0])
drawrobot3d4(teta, d, a, alfa)

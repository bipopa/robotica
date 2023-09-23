from planifica4 import planifica4
from animacion4 import animacion4
import numpy as np
from inversekinematic4 import inversekinematic4
from directkinematic4 import directkinematic4
from drawrobot3d4 import drawrobot3d4

p1=[0, 0, 0]
p2=[0.2, -0.4, 0.4]
n=[1, 0, 0]
s=[0, 1, 0]
a=[0, 0, 1]
npuntos=100

q = np.array([0.0 ,  0.0,  0.0,  0.0])
teta = np.array([q[0], 0, 0, q[3]])
d = np.array([0.4, q[1], q[2], 0.2])
al = np.array([0, -0.1, 0, 0])
alfa = np.array([0, -np.pi/2, 0, 0])
drawrobot3d4(teta, d, al, alfa)
A04 = directkinematic4(teta, d, al, alfa)
mat_q=planifica4(p1, p2, n, s, a, npuntos,teta,d,al,alfa)
#print(mat_q)
animacion4(mat_q,teta,d,al,alfa)




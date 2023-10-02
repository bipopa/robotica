
#completo
#SIN ERRORES

from planifica4 import planifica4
from animacion4 import animacion4
import numpy as np
from inversekinematic4 import inversekinematic4
from directkinematic4 import directkinematic4
from drawrobot3d4 import drawrobot3d4
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import time

#ESTO CAMBIA CON LA INV

p1=[0.8, -1, 0.8]
p2=[0.8, -1, 0.4]
p3=[0.5,-1,0.4]
p4=[0.5,-1,0.8]
p5=[0.3,-1,0.4]
p6=[0.3,-1,0.8]
p7=[0,-1,0.8]
p8=[0,-1,0.4]
p9=[0.3,-1,0.6]
p10=[0,-1,0.6]
p11=[-0.2,-1,0.4]
p12=[-0.2,-1,0.8]
p13=[-0.5,-1,0.8]
p14=[-0.5,-1,0.4]

n=[1, 0, 0]
s=[0, 1, 0]
a=[0, 0, 1]
npuntos=20

q = [0, np.pi/2, 0, 0,np.pi/2,0]

teta = np.array([q[0], q[1], q[2], q[3],q[4],q[5]])
d = np.array([0.223, 0, 0, 0.172, 0,0.1052])
al = np.array([0, 0.083, 0, 0, 0, 0])
alfa = np.array([np.pi/2, 0, np.pi/2, np.pi/2, np.pi/2, 0])
drawrobot3d4(teta, d, al, alfa)
A04 = directkinematic4(teta, d, al, alfa)


x0, y0, z0 = 0, 0, 0
    # Se dibuja el sistema de coordenadas de referencia

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
p, = ax.plot([x0], [y0], [z0], 'b', linewidth=2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
    # Se asigna una rejilla a los ejes
ax.grid(True)
    # Se establecen los límites de los ejes
ax.set_xlim3d([-1, 1])
ax.set_ylim3d([-1, 1])
ax.set_zlim3d([0, 1.5])
    # Mantiene el gráfico actual
plt.ion()
plt.show()

plt.plot([1,1,-0.7,-0.7,1],[-1,-1,-1,-1,-1],[0,1,1,0,0],color="red",linewidth="2")

u1=planifica4(p1, p2, n, s, a, npuntos,teta,d,al,alfa)
u2=planifica4(p2, p3, n, s, a, npuntos,teta,d,al,alfa)
u3=planifica4(p3, p4, n, s, a, npuntos,teta,d,al,alfa)
es1=planifica4(p4, p5, n, s, a, npuntos,teta,d,al,alfa)
a1=planifica4(p5, p6, n, s, a, npuntos,teta,d,al,alfa)
a2=planifica4(p6, p7, n, s, a, npuntos,teta,d,al,alfa)
a3=planifica4(p7, p8, n, s, a, npuntos,teta,d,al,alfa)
es2=planifica4(p8, p9, n, s, a, npuntos,teta,d,al,alfa)
a4=planifica4(p9, p10, n, s, a, npuntos,teta,d,al,alfa)
es3=planifica4(p10, p11, n, s, a, npuntos,teta,d,al,alfa)
o1=planifica4(p11, p12, n, s, a, npuntos,teta,d,al,alfa)
o2=planifica4(p12, p13, n, s, a, npuntos,teta,d,al,alfa)
o3=planifica4(p13, p14, n, s, a, npuntos,teta,d,al,alfa)
o4=planifica4(p14, p11, n, s, a, npuntos,teta,d,al,alfa)
oo=planifica4(p11,p1,n,s,a,npuntos,teta,d,al,alfa)
#print(mat_q)
animacion4(u1,teta,d,al,alfa,ax,p,1)
animacion4(u2,teta,d,al,alfa,ax,p,1)
animacion4(u3,teta,d,al,alfa,ax,p,1)
animacion4(es1,teta,d,al,alfa,ax,p,0)
animacion4(a1,teta,d,al,alfa,ax,p,1)
animacion4(a2,teta,d,al,alfa,ax,p,1)
animacion4(a3,teta,d,al,alfa,ax,p,1)
animacion4(es2,teta,d,al,alfa,ax,p,0)
animacion4(a4,teta,d,al,alfa,ax,p,1)
animacion4(es3,teta,d,al,alfa,ax,p,0)
animacion4(o1,teta,d,al,alfa,ax,p,1)
animacion4(o2,teta,d,al,alfa,ax,p,1)
animacion4(o3,teta,d,al,alfa,ax,p,1)
animacion4(o4,teta,d,al,alfa,ax,p,1)
animacion4(oo,teta,d,al,alfa,ax,p,0)


while True:
        time.sleep(1)


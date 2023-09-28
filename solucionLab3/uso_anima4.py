from planifica4 import planifica4
from animacion4 import animacion4
import numpy as np
from inversekinematic4 import inversekinematic4
from directkinematic4 import directkinematic4
from drawrobot3d4 import drawrobot3d4
import time

p1=[0, 0, 0]
p2=[-0.7, -0.5, 1.2]
p3=[-0.7, -0.5, 0.5]
p4=[-0.3, -0.5, 0.5]
p5=[-0.3, -0.5, 1.2]
p6=[0,-0.5,0.5]
p7=[0,-0.5,1.2]
p8=[0.3,-0.5,1.2]
p9=[0.3,-0.5,0.5]
p10=[0.3,-0.5,0.8]
p11=[0,-0.5,0.8]
p12=[0.6,-0.5,1.2]
p13=[0.9,-0.5,1.2]
p14=[0.9,-0.5,0.5]
p15=[0.6,-0.5,0.5]

n=[1, 0, 0]
s=[0, 1, 0]
a=[0, 0, 1]

npuntos=100

q = np.array([0.0 ,  0.0,  0.0,  0.0])
teta = np.array([q[0], 0, 0, q[3]])
d = np.array([0.4, q[1], q[2], 0.2])
al = np.array([0, -0.1, 0, 0])
alfa = np.array([0, -np.pi/2, 0, 0])
A04 = directkinematic4(teta, d, al, alfa)

mat_q=planifica4(p1, p2, n, s, a, npuntos,teta,d,al,alfa)
print(mat_q)
mat_q1=planifica4(p2, p3, n, s, a, npuntos,teta,d,al,alfa)
print(mat_q1)
mat_q2=planifica4(p3, p4, n, s, a, npuntos,teta,d,al,alfa)
print(mat_q2)
mat_q3=planifica4(p4, p5, n, s, a, npuntos,teta,d,al,alfa)
print(mat_q3)
mat_q4=planifica4(p5, p6, n, s, a, npuntos,teta,d,al,alfa)
print(mat_q4)
mat_q5=planifica4(p6, p7, n, s, a, npuntos,teta,d,al,alfa)
print(mat_q5)
mat_q6=planifica4(p7, p8, n, s, a, npuntos,teta,d,al,alfa)
print(mat_q6)
mat_q7=planifica4(p8, p9, n, s, a, npuntos,teta,d,al,alfa)
print(mat_q7)
mat_q8=planifica4(p9, p10, n, s, a, npuntos,teta,d,al,alfa)
print(mat_q8)
mat_q9=planifica4(p10, p11, n, s, a, npuntos,teta,d,al,alfa)
print(mat_q9)
mat_q10=planifica4(p11, p12, n, s, a, npuntos,teta,d,al,alfa)
print(mat_q10)
mat_q11=planifica4(p12, p13, n, s, a, npuntos,teta,d,al,alfa)
print(mat_q11)
mat_q12=planifica4(p13, p14, n, s, a, npuntos,teta,d,al,alfa)
print(mat_q12)
mat_q13=planifica4(p14, p15, n, s, a, npuntos,teta,d,al,alfa)
print(mat_q13)
mat_q14=planifica4(p15, p12, n, s, a, npuntos,teta,d,al,alfa)
print(mat_q14)
animacion4(mat_q,mat_q1,mat_q2,mat_q3,mat_q4,mat_q5,mat_q6,mat_q7,mat_q8,mat_q9,mat_q10,mat_q11,mat_q12,mat_q13,mat_q14,teta,d,al,alfa)


while(True):
	time.sleep(0)

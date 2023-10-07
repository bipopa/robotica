from planifica import planifica
from animacion import animacion,animatest
import numpy as np
import time
from animaciones import animaciones
from matriz_rotacion import rot_x, rot_y,rot_z,matriz_rotacion

#valores para las rotaciones en radianes
Rx=rot_x(0)
Rz=rot_z(0)
Ry=rot_y(0)
##letra U
p1=[-0.5,-0.05,0.3] #matq
p2=[-0.5, -0.05, 0]#matq-q1
p3=[-0.4, -0.05 ,0]#matq1-q2
p4=[-0.4, -0.05, 0.01]#matq2-q3
p5=[-0.4, -0.05 ,0.3]#matq3-q4

#letra A
p6=[-0.3, -0.05, 0.0]#matq4-q5
p7=[-0.3, -0.05, 0.3]#matq5-q6
p8=[-0.2, -0.05, 0.3]#matq6-q7
p9=[-0.2, -0.05, 0.0]#matq7-q8
p10=[-0.2, -0.05, 0.15]#matq8-q9
p11=[-0.3,-0.05,0.15]#matq9-q10
#letra O
p12=[-0.1,-0.05,0.0]#matq9-q11
p13=[-0.1,-0.05,0.3]#matq9-q12
p14=[0.0,-0.05,0.3]#matq9-q13
p15=[0.0,-0.05,0.0]#matq9-q14
p16=[-0.1,-0.05,0.0]
##generar rotaciones en Y
p1=np.matmul(Ry,p1)
p2=np.matmul(Ry,p2)
p3=np.matmul(Ry,p3)
p4=np.matmul(Ry,p4)
p5=np.matmul(Ry,p5)
p6=np.matmul(Ry,p6)
p7=np.matmul(Ry,p7)
p8=np.matmul(Ry,p8)
p9=np.matmul(Ry,p9)
p10=np.matmul(Ry,p10)
p11=np.matmul(Ry,p11)
p12=np.matmul(Ry,p12)
p13=np.matmul(Ry,p13)
p14=np.matmul(Ry,p14)
p15=np.matmul(Ry,p15)
p16=np.matmul(Ry,p16)
##generar rotaciones en X
p1=np.matmul(Rx,p1)
p2=np.matmul(Rx,p2)
p3=np.matmul(Rx,p3)
p4=np.matmul(Rx,p4)
p5=np.matmul(Rx,p5)
p6=np.matmul(Rx,p6)
p7=np.matmul(Rx,p7)
p8=np.matmul(Rx,p8)
p9=np.matmul(Rx,p9)
p10=np.matmul(Rx,p10)
p11=np.matmul(Rx,p11)
p12=np.matmul(Rx,p12)
p13=np.matmul(Rx,p13)
p14=np.matmul(Rx,p14)
p15=np.matmul(Rx,p15)
p16=np.matmul(Rx,p16)
##generar rotaciones en z
p1=np.matmul(Rz,p1)
p2=np.matmul(Rz,p2)
p3=np.matmul(Rz,p3)
p4=np.matmul(Rz,p4)
p5=np.matmul(Rz,p5)
p6=np.matmul(Rz,p6)
p7=np.matmul(Rz,p7)
p8=np.matmul(Rz,p8)
p9=np.matmul(Rz,p9)
p10=np.matmul(Rz,p10)
p11=np.matmul(Rz,p11)
p12=np.matmul(Rz,p12)
p13=np.matmul(Rz,p13)
p14=np.matmul(Rz,p14)
p15=np.matmul(Rz,p15)
p16=np.matmul(Rz,p16)
#Orientación del robot, asegurese de cambiar estos parametros dependiendo del plano en el que desea dibujar
###########
n=[0.05999119, 0.02659445, -0.99784457]
s=[-0.05663413, -0.99794411, -0.03000199 ]   
a=[-0.99659101, 0.05831192, -0.0583617]
###########

nsa=[[n],[s],[a]]

nsarot=np.matmul(nsa,Ry)

#rotación orientación en y

n=np.matmul(n,Ry)
s=np.matmul(s,Ry)
a=np.matmul(a,Ry)
#######
#rotación orientación en x

n=np.matmul(n,Rx)
s=np.matmul(s,Rx)
a=np.matmul(a,Rx)
#######
#rotación orientación en z

n=np.matmul(n,Rz)
s=np.matmul(s,Rz)
a=np.matmul(a,Rz)
#######
print("nSA",nsarot)
npuntos=10

l0 = 0.17
l1 = 0.22
l2 = 0.22
l3 = 0.1052

q = [0, 0, 0, 0, 0, 0]


#drawrobot3d4(q, l0, l1, l2,l3)
#letra U
mat_q=planifica(p1, p2, n, s, a, npuntos,l0,l1,l2,l3)
mat_q1=planifica(p2, p3, n, s, a, npuntos,l0,l1,l2,l3)
mat_q2=planifica(p3, p4, n, s, a, npuntos,l0,l1,l2,l3)
mat_q3=planifica(p4, p5, n, s, a, npuntos,l0,l1,l2,l3)
#viaje U-A
mat_q4=planifica(p5, p6, n, s, a, npuntos,l0,l1,l2,l3)
#letra A
mat_q5=planifica(p6, p7, n, s, a, npuntos,l0,l1,l2,l3)
mat_q6=planifica(p7, p8, n, s, a, npuntos,l0,l1,l2,l3)
mat_q7=planifica(p8, p9, n, s, a, npuntos,l0,l1,l2,l3)
#viaja A-A
mat_q8=planifica(p9, p10, n, s, a, npuntos,l0,l1,l2,l3)
#linea A
mat_q9=planifica(p10, p11, n, s, a, npuntos,l0,l1,l2,l3)
#viaje A-O
mat_q10=planifica(p11, p12, n, s, a, npuntos,l0,l1,l2,l3)
##letra O
mat_q11=planifica(p12, p13, n, s, a, npuntos,l0,l1,l2,l3)
mat_q12=planifica(p13, p14, n, s, a, npuntos,l0,l1,l2,l3)
mat_q13=planifica(p14, p15, n, s, a, npuntos,l0,l1,l2,l3)
mat_q14=planifica(p15, p16, n, s, a, npuntos,l0,l1,l2,l3)


#animacion(mat_q,l0,l1,l2,l3)
#animacion(mat_q2,l0,l1,l2,l3)
#animacion(mat_q3,l0,l1,l2,l3)
#animacion(mat_q4,l0,l1,l2,l3)
#animacion(mat_q5,l0,l1,l2,l3)

#animación UAO
animaciones(mat_q,mat_q1,mat_q2,mat_q3,mat_q4,mat_q5,mat_q6,mat_q7,mat_q8,mat_q9,mat_q10,mat_q11,mat_q12,mat_q13,mat_q14 ,l0,l1,l2,l3)
while True:
    time.sleep(1)
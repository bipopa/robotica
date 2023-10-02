import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from denavit import Tdh
from drawrobot3d4 import drawrobot3d4
import time
#Este metodo permite visualizar el metodo del robot
def animacion4(mat_q,teta,d,a,alfa,ax,p,t):
    # Parámetros Tdh-Hartenberg del robot
    # d = np.array([0.315, 0, 0, 0.5, 0, 0.08])
    # a = np.array([0, 0.45, 0, 0, 0, 0])
    # alfa = np.array([-np.pi/2, 0, np.pi/2, -np.pi/2, np.pi/2, 0])
    # Vector de posicion (x, y, z) del sistema de coordenadas de referencia

    # Número de columnas de la matriz
    n = mat_q.shape[1]
    # Se dibuja la disposición del robot correspondiente a cada columna
    for i in range(n):
        # Variables articulares del brazo robot
        teta[0] = mat_q[0,i] 
        teta[3] = mat_q[3,i] #DE PRONTO CAMBIA
        

        d[1] =  mat_q[1,i]
        d[2] =  mat_q[2,i]
        

        #drawrobot3d4(teta, d, a, alfa)
        #input()
        # Matrices de transformación del primer sistema al correspondiente
        A01 = Tdh(teta[0], d[0], a[0], alfa[0])
        A12 = Tdh(teta[1], d[1], a[1], alfa[1])
        A23 = Tdh(teta[2], d[2], a[2], alfa[2])
        A34 = Tdh(teta[3], d[3], a[3], alfa[3])
        A45 = Tdh(teta[4], d[4], a[4], alfa[4])
        A56 = Tdh(teta[5], d[5], a[5], alfa[5])
    # Matrices de transformación del primer sistema al correspondiente
        A02 = np.dot(A01, A12)
        A03 = np.dot(A02, A23)
        A04 = np.dot(A03, A34)
        A05 = np.dot(A04, A45)
        A06 = np.dot(A05, A56)
    # Vector de posicion (x, y, z) de cada sistema de coordenadas
        x0, y0, z0 = 0, 0, 0
        x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
        #xi, yi, zi = x1, y1, z1 + d[1]
        x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
        x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
        x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
        x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
        x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
    # Se dibuja el robot
        x = [x0, x1, x2, x3, x4, x5, x6]
        y = [y0, y1, y2, y3, y4, y5, y6]
        z = [z0, z1, z2, z3, z4, z5, z6]

    
        ax.grid(True)
    # Se establecen los límites de los ejes
   
        p.set_data(x, y)
        p.set_3d_properties(z)
      #  ax.scatter(x, y, z)
        # Se fuerza a Python a actualizar la pantalla
        if(t==1):
            plt.plot(x6,y6,z6 ,marker=".", color="black")
            plt.title('Elaborado por el buen Byron')
        
        plt.pause(0.15)
    #while True:
     #   time.sleep(1)
    # Código que se ejecutará infinitamente
    
    
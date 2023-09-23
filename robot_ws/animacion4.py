import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from denavit import denavit
from drawrobot3d4 import drawrobot3d4
import time
def animacion4(mat_q,teta,d,a,alfa):
    # Parámetros Denavit-Hartenberg del robot
    # d = np.array([0.315, 0, 0, 0.5, 0, 0.08])
    # a = np.array([0, 0.45, 0, 0, 0, 0])
    # alfa = np.array([-np.pi/2, 0, np.pi/2, -np.pi/2, np.pi/2, 0])
    # Vector de posicion (x, y, z) del sistema de coordenadas de referencia
    x0, y0, z0 = 0, 0, 0
    # Se dibuja el sistema de coordenadas de referencia
    

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    p, = ax.plot([x0], [y0], [z0], 'r', linewidth=2)
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
    # Número de columnas de la matriz
    n = mat_q.shape[1]
    # Se dibuja la disposición del robot correspondiente a cada columna
    for i in range(n):
        # Variables articulares del brazo robot
        teta[0] = mat_q[0,i]
        teta[3] = mat_q[3,i]
        d[1] =  mat_q[1,i]
        d[2] =  mat_q[2,i]

        #drawrobot3d4(teta, d, a, alfa)
        #input()
        # Matrices de transformación del primer sistema al correspondiente
        A01 = denavit(teta[0], d[0], a[0], alfa[0])
        A12 = denavit(teta[1], d[1], a[1], alfa[1])
        A23 = denavit(teta[2], d[2], a[2], alfa[2])
        A34 = denavit(teta[3], d[3], a[3], alfa[3])
    # Matrices de transformación del primer sistema al correspondiente
        A02 = np.dot(A01, A12)
        A03 = np.dot(A02, A23)
        A04 = np.dot(A03, A34)
    # Vector de posicion (x, y, z) de cada sistema de coordenadas
        x0, y0, z0 = 0, 0, 0
        x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
        xi, yi, zi = x1, y1, z1 + d[1]
        x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
        x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
        x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
    # Se dibuja el robot
        x = [x0, x1, xi, x2, x3, x4]
        y = [y0, y1, yi, y2, y3, y4]
        z = [z0, z1, zi, z2, z3, z4]
    
        ax.grid(True)
    # Se establecen los límites de los ejes
   
        p.set_data(x, y)
        p.set_3d_properties(z)
      #  ax.scatter(x, y, z)
        # Se fuerza a Python a actualizar la pantalla
        plt.pause(0.1)
    while True:
        time.sleep(1)
    # Código que se ejecutará infinitamente

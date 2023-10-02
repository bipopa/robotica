import numpy as np
import matplotlib.pyplot as plt
from denavit import denavit


def drawrobot3d4(teta, d, a, alfa):
    # Parámetros Denavit-Hartenberg del robot
    # teta = [q[0], 0, 0, q[3]]
    # d = [0.4, q[1], q[2], 0.2]
    # a = [0, -0.1, 0, 0]
    # alfa = [0, -np.pi/2, 0, 0]
    # Matrices de transformación homogénea entre sistemas de coordenadas consecutivos
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
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    ax.scatter(x, y, z)
    # Se coloca una rejilla a los ejes
    ax.grid(True)
    # Se establecen los límites de los ejes
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([0, 1.5])
    plt.show()

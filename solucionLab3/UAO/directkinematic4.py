""" 
DIRECTKINEMATIC4 Direct Kinematic.
A04 = DIRECTKINEMATIC4(Q) devuelve la matriz de transformación del
primer sistema de coordenadas al último en función del vector Q 
de variables articulares
 """

import numpy as np
from denavit import denavit

def directkinematic4(teta, d, a, alfa):
    # Denavit-Hartenberg parameters of the robot
    #teta = np.array([q[0], 0, 0, q[3]])
    #d = np.array([0.4, q[1], q[2], 0.2])
    #a = np.array([0, -0.1, 0, 0])
    #alfa = np.array([0, -np.pi/2, 0, 0])
    
    # Homogeneous transformation matrices between consecutive coordinate systems
    A01 = denavit(teta[0], d[0], a[0], alfa[0])
    A12 = denavit(teta[1], d[1], a[1], alfa[1])
    A23 = denavit(teta[2], d[2], a[2], alfa[2])
    A34 = denavit(teta[3], d[3], a[3], alfa[3])
    
    # Transformation matrix from the first to the last coordinate system
    A04 = np.dot(np.dot(np.dot(A01, A12), A23), A34)
    return A04

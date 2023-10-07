
#COMPLETO
#SIN ERRORES
import numpy as np
from inversekinematic import cinematica_inversa_centaurirad

def planifica(p1, p2, n, s, a, npuntos,l0,l1,l2,l3):
    # Cálculo del vector unitario
    u = np.array(p2) - np.array(p1)
    mu = np.sqrt(u[0]**2 + u[1]**2 + u[2]**2)
    u = (1 / mu) * u
    
    # Cálculo de la distancia entre puntos
    dl = mu / (npuntos + 1)
    
    # Inicialización de la matriz mat_q
    mat_q = np.zeros((6, npuntos + 2))
    #print(mat_q)
    for i in range(npuntos + 2):
        # Cálculo de la posición cartesiana actual de la mano del manipulador
        p = p1 + (i * dl) * u
        
        Tr = np.array([n, s, a, p]).T
        # Cálculo de las coordenadas articulares
       
        q = cinematica_inversa_centaurirad(Tr,l0,l1,l2,l3)
        mat_q[:, i] = q.flatten()
        #print(q)
        #input()
    return mat_q

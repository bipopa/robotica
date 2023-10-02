
#completo
#SIN ERRORES

import numpy as np
from directkinematic4 import directkinematic4
import sympy as sp
from sympy import *

#Imprimir una matriz de un robot de 4 grados grados de libertad
#Se usa de ejemplo
#De verificacion
l0=sp.Symbol('l0')
l1=sp.Symbol('l1')
l2=sp.Symbol('l2')
l3=sp.Symbol('l3')

q1 = sp.Symbol('q1')
q2 = sp.Symbol('q2')
q3 = sp.Symbol('q3')
q4 = sp.Symbol('q4')
q5 = sp.Symbol('q5')
q6 = sp.Symbol('q6')

# Ejemplo de uso
q = [0, np.pi/2, 0, 0,np.pi/2,0]

teta = np.array([q[0], q[1], q[2], q[3],q[4],q[5]])
d = np.array([0.223, 0, 0, 0.172, 0,0.1052])
a = np.array([0, 0.083, 0, 0, 0, 0])
alfa = np.array([np.pi/2, 0, np.pi/2, np.pi/2, np.pi/2, 0])
A06 = directkinematic4(teta, d, a, alfa)

# Imprimir la matriz de transformación homogénea
print(A06)

# Cinemática directa del robot
import numpy as np
from denavit import Tdh
def cdirecta_centauri(q, l0,l1, l2, l3):
    """ Retorna los sistemas de referencia de cada eslabón con respecto a la base
    """
    # Transformaciones homogéneas de DH
    T01 = Tdh(l0, q[0], 0, np.pi/2)
    T12 = Tdh(0, np.pi/2+q[1], l1, 0)
    T23 = Tdh(0, np.pi/2+q[2], 0, np.pi/2)
    T34 = Tdh(l2, q[3], 0, -np.pi/2)
    T45 = Tdh(0, q[4], 0, np.pi/2)
    T56 = Tdh(l3, q[5], 0, 0)
    # Efector final con respecto a la base
    #Tf = T01.dot(T12).dot(T23)
    Tf = T01.dot(T12).dot(T23).dot(T34).dot(T45).dot(T56)
    print(Tf)
    return Tf

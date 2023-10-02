import numpy as np
from directkinematic import cdirecta_centauri
# Ejemplo de cálculo de la cinemática directa
l0 = 0.17                              # Longitud eslabón 1
l1 = 0.22                               # Longitud eslabón 2
l2 = 0.22                               # Longitud eslabón 3 
l3 = 0.1
q = [np.deg2rad(45.001), np.deg2rad(13), np.deg2rad(40), np.deg2rad(180),np.deg2rad(0.01), np.deg2rad(-40.001)]    # Valores articulares
print(q)
# Cinemática directa
Te = cdirecta_centauri(q, l0, l1, l2, l3)   # Cinemática directa

# Mostrar el resultado
print("Efector final con respecto a la base cuando q1={}, q2={}, q3={}, q4={}, q5={}, q6={}".format(np.rad2deg(q[0]), np.rad2deg(q[1]), 
                                                          np.rad2deg(q[2]), np.rad2deg(q[3]), np.rad2deg(q[4]), np.rad2deg(q[5]) ))
print(np.round(Te,4))



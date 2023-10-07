import numpy as np
from matriz_rotacion import matriz_rotacion
from directkinematic import cdirecta_centauri
from angulos_euler import obtener_angulos_euler
# Ejemplo de cálculo de la cinemática directa
l0 = 0.17                              # Longitud eslabón 1
l1 = 0.22                               # Longitud eslabón 2
l2 = 0.22                               # Longitud eslabón 3 
l3 = 0.1
q = [np.deg2rad(45.001), np.deg2rad(13), np.deg2rad(40), np.deg2rad(180),np.deg2rad(0.01), np.deg2rad(-40.001)]    # Valores articulares
# Ángulos de Euler en radianes
pitch = np.deg2rad(-37.712588369867824)
roll = np.deg2rad(40.45475900303179)
yaw = np.deg2rad(-9.345011407518152)
Te = cdirecta_centauri(q, l0, l1, l2, l3)   # Cinemática directa
yaw, pitch, roll =obtener_angulos_euler(Te[:3, :3])

yaw, pitch, roll =obtener_angulos_euler(Te[:3, :3])

print("yaw",np.degrees(yaw),"pitch",np.degrees(pitch),"roll",np.degrees(roll))
# Calcular la matriz de rotación
matriz_rot = matriz_rotacion(yaw, pitch, roll)
print("rpy",np.round(matriz_rot,4))

Tdes = np.identity(4)  # Matriz de identidad 4x4
Tdes[:3, :3] = matriz_rot
#coordenadas de posicion
Tdes[:3, 3] = Te[:3, 3]
print (Tdes, "tdes1")

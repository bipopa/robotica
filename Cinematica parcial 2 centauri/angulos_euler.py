import numpy as np
def obtener_angulos_euler(matriz_rotacion):
    # Calcular el ángulo de Yaw (rotación alrededor del eje Z)
    yaw = np.arctan2(matriz_rotacion[1, 0], matriz_rotacion[0, 0])

    # Calcular el ángulo de Pitch (rotación alrededor del eje Y)
    pitch = np.arctan2(-matriz_rotacion[2, 0], np.sqrt(matriz_rotacion[2, 1] ** 2 + matriz_rotacion[2, 2] ** 2))

    # Calcular el ángulo de Roll (rotación alrededor del eje X)
    roll = np.arctan2(matriz_rotacion[2, 1], matriz_rotacion[2, 2])

    # Convertir los ángulos de radianes a grados si es necesario
    yaw_degrees = np.degrees(yaw)
    pitch_degrees = np.degrees(pitch)
    roll_degrees = np.degrees(roll)

    return yaw, pitch, roll,yaw_degrees,pitch_degrees,roll_degrees 
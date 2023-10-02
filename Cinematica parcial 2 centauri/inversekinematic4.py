import numpy as np
def matriz_rotacion(yaw, pitch, roll):
    Rz = np.array([[np.cos(yaw), -np.sin(yaw), 0],
                   [np.sin(yaw), np.cos(yaw), 0],
                   [0, 0, 1]])

    Ry = np.array([[np.cos(pitch), 0, np.sin(pitch)],
                   [0, 1, 0],
                   [-np.sin(pitch), 0, np.cos(pitch)]])

    Rx = np.array([[1, 0, 0],
                   [0, np.cos(roll), -np.sin(roll)],
                   [0, np.sin(roll), np.cos(roll)]])

    # La matriz de rotación total es R = Rz * Ry * Rx (ZYX)
    R = np.dot(Rz, np.dot(Ry, Rx))

    return R

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

    return yaw, pitch, roll

def Tdh(d, th, a, alpha):
    cth = np.cos(th);    sth = np.sin(th)
    ca = np.cos(alpha);  sa = np.sin(alpha)
    Tdh = np.array([[cth, -ca*sth,  sa*sth, a*cth],
                    [sth,  ca*cth, -sa*cth, a*sth],
                    [0,        sa,     ca,      d],
                    [0,         0,      0,      1]])
    return Tdh

# Cinemática directa del robot
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

    return Tf

def cinematica_inversa_centauri(Tdes,l0,l1,l2,l3):
    pmx= Tdes[0,3]-l3*Tdes[0,2]
    pmy= Tdes[1,3]-l3*Tdes[1,2]
    pmz= Tdes[2,3]-l3*Tdes[2,2]
    print("pmx=",pmx, "pmy=", pmy, "pmz=", pmz)
    q1=np.arctan2(pmy,pmx)
    if q1<0:
        q1+=np.pi
    R=np.sqrt(pmx**2+pmy**2+(pmz-l0)**2)
    r=np.sqrt(pmx**2+pmy**2)
    #print("R=",R, "r=", r)
    # Valores articulares calculados
    #calpha=(R)/(2*l1)
    
    #alpha= np.arctan2(np.sqrt(1-calpha**2),calpha)
    #print("alpha",np.degrees(aalpha))
    #beta= -np.arctan2(pmz-l0,r)
    #print("beta",np.degrees(beta))
    #q2=0*np.pi/2-beta-alpha
    cq3 = (R**2-l1**2-l2**2)/(2*l1*l2)
    q3 = np.arctan2(np.sqrt(1-cq3**2),cq3)
    q2 = np.pi/2+np.arctan2(-pmz+l0,r)-np.arctan2(l2*np.sin(q3),l1+l2*np.cos(q3))
    # Resultado
    #print(np.degrees(q1))
    ROT03=[[-np.cos(q1)*np.cos(q2 + q3), np.sin(q1), -np.sin(q2 + q3)*np.cos(q1)], 
[-np.sin(q1)*np.cos(q2 + q3), -np.cos(q1), -np.sin(q1)*np.sin(q2 + q3)], 
[-np.sin(q2 + q3), 0, np.cos(q2 + q3)]] 
    #print(np.round(ROT03,4))
    
    ROT06=Tdes[0:3,0:3]
    #print(np.round(ROT06,4))
    ROT36=np.transpose(ROT03) .dot(ROT06)
    #print(np.round(ROT36,4))
    nx= ROT36[0,0]
    ox= ROT36[0,1]
    ax= ROT36[0,2]
    ny= ROT36[1,0]
    oy= ROT36[1,1]
    ay= ROT36[1,2]
    nz= ROT36[2,0]
    oz= ROT36[2,1]
    az= ROT36[2,2]
    q4=np.arctan2(ay,ax)
    q5=np.arctan2(ay/np.sin(q4),az)
    q6=np.arctan2(oz,-nz)

    return (np.degrees(q1), np.degrees(q2), np.degrees(q3), np.degrees(q4), np.degrees(q5), np.degrees(q6))

# Ejemplo de cálculo de la cinemática directa
l0 = 0.17                              # Longitud eslabón 1
l1 = 0.22                               # Longitud eslabón 2
l2 = 0.22                               # Longitud eslabón 3 
l3 = 0.1
q = [np.deg2rad(45.001), np.deg2rad(13), np.deg2rad(40), np.deg2rad(180),np.deg2rad(0.01), np.deg2rad(-40.001)]    # Valores articulares

# Cinemática directa
Te = cdirecta_centauri(q, l0, l1, l2, l3)   # Cinemática directa

# Mostrar el resultado
print("Efector final con respecto a la base cuando q1={}, q2={}, q3={}, q4={}, q5={}, q6={}".format(np.rad2deg(q[0]), np.rad2deg(q[1]), 
                                                          np.rad2deg(q[2]), np.rad2deg(q[3]), np.rad2deg(q[4]), np.rad2deg(q[5]) ))
print(np.round(Te,4))



# Ángulos de Euler en radianes
pitch = np.deg2rad(-37.712588369867824)
roll = np.deg2rad(40.45475900303179)
yaw = np.deg2rad(-9.345011407518152)

#yaw, pitch, roll =obtener_angulos_euler(Te[:3, :3])

print("yaw",np.degrees(yaw),"pitch",np.degrees(pitch),"roll",np.degrees(roll))
# Calcular la matriz de rotación
matriz_rot = matriz_rotacion(yaw, pitch, roll)
print("rpy",np.round(matriz_rot,4))

Tdes = np.identity(4)  # Matriz de identidad 4x4
Tdes[:3, :3] = matriz_rot
#coordenadas de posicion
Tdes[:3, 3] = Te[:3, 3]
Tdes[:3, 3] = np.array([-0.16, -0.16, 0.620])

#ejemplo de uso cinematica inversa
z=cinematica_inversa_centauri(Tdes,l0,l1,l2,l3)
print(z)

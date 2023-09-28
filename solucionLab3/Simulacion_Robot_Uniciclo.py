from pyRobotics import *
import time
#################### TIEMPO ###################

tf = 60 # tiempo de simulacion
ts = 0.1 #  tiempo de muestreo
t = np.arange(0,tf+ts,ts) # vector tiempo

N = len(t) # cantidad de muestras

################### CONDICIONES INICIALES ###################

# Asignar memoria 
hx = np.zeros(N+1) 
hy = np.zeros(N+1)
phi = np.zeros(N+1)

hx[0] = 0;  # Posicion inicial en el eje x en metros [m]
hy[0] = 0;  # Posicion inicial en el eje y en metros [m]
phi[0] = 0*(np.pi/180) # Orientacion inicial en radianes [rad]

################### VELOCIDADES DE REFERENCIA #################### 

uRef = 0.1*np.ones(N) # Velocidad lineal en metros/segundos [m/s]
wRef = 0.2*np.ones(N)# Velocidad angular en radianes/segundos [rad/s]


################### BUCLE ####################  
for k in range(N):
     
     # Integral numerica
     phi[k+1] = phi[k]+ts*wRef[k]

     # Modelo cinemático
     
     hxp = uRef[k]*np.cos(phi[k+1])
     hyp = uRef[k]*np.sin(phi[k+1])
     
     # Integral numerica
     hx[k+1] = hx[k] + ts*hxp
     hy[k+1] = hy[k] + ts*hyp

################### SIMULACION VIRTUAL #################### 

pathStl = "stl"
color = ['yellow','black','gray','gray','white','blue']
uniciclo = robotics(pathStl,color)

xmin = -1
xmax = 1
ymin = -0.5
ymax = 1.5
zmin = 0
zmax = 1
bounds = [xmin, xmax, ymin, ymax, zmin, zmax]
uniciclo.configureScene(bounds)

uniciclo.initTrajectory(hx,hy)

escala = 2
uniciclo.initRobot(hx,hy,phi,escala)

uniciclo.startSimulation(1,ts)





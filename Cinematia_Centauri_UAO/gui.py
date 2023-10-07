import numpy as np
import matplotlib.pyplot as plt
from denavit import Tdh
from matplotlib.widgets import Button, Slider

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

l0 = 0.17
l1 = 0.22
l2 = 0.22
l3 = 0.1052

q = [0, 0, 0, 0, 0, 0]

teta = np.array([q[0], q[1]+np.pi/2, q[2]+np.pi/2, q[3],q[4],q[5]])
d = np.array([l0, 0, 0, l2, 0,l3])
a = np.array([0, l1, 0, 0, 0, 0])
alfa = np.array([np.pi/2, 0, np.pi/2, -np.pi/2, np.pi/2, 0])



A01 = Tdh(teta[0], d[0], a[0], alfa[0])
A12 = Tdh(teta[1], d[1], a[1], alfa[1])
A23 = Tdh(teta[2], d[2], a[2], alfa[2])
A34 = Tdh(teta[3], d[3], a[3], alfa[3])
A45 = Tdh(teta[4], d[4], a[4], alfa[4])
A56 = Tdh(teta[5], d[5], a[5], alfa[5])
# Matrices de transformación del primer sistema al correspondiente
A02 = np.dot(A01, A12)
A03 = np.dot(A02, A23)
A04 = np.dot(A03, A34)
A05 = np.dot(A04, A45)
A06 = np.dot(A05, A56)

# Vector de posicion (x, y, z) de cada sistema de coordenadas
x0, y0, z0 = 0, 0, 0
x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
# Se dibuja el robot
x = [x0, x1, x2, x3, x4, x5, x6]
y = [y0, y1, y2, y3, y4, y5, y6]
z = [z0, z1, z2, z3, z4, z5, z6]

print("T06: ", A06)


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

# adjust the main plot to make room for the sliders
fig.subplots_adjust(bottom=0.4)

# Make a horizontal slider to control the frequency.
ax_q1 = fig.add_axes([0.2, 0.1, 0.65, 0.03])
ax_q2 = fig.add_axes([0.2, 0.15, 0.65, 0.03])
ax_q3 = fig.add_axes([0.2, 0.20, 0.65, 0.03])
ax_q4 = fig.add_axes([0.2, 0.25, 0.65, 0.03])
ax_q5 = fig.add_axes([0.2, 0.30, 0.65, 0.03])
ax_q6 = fig.add_axes([0.2, 0.35, 0.65, 0.03])


# create the sliders
q1 = Slider(
	ax_q1, "q1", -np.pi/2,np.pi/2,
	valinit=0, valstep=0.1,
	color="green"
)

q2 = Slider(
	ax_q2, "q2", -np.pi/2, np.pi/2,
	valinit=0, valstep=0.1,
	initcolor='none'  # Remove the line marking the valinit position.
)

q3 = Slider(
	ax_q3, "q3", -np.pi/2, np.pi/2,
	valinit= 0, valstep=0.1,
	initcolor='none'  # Remove the line marking the valinit position.
)
q4 = Slider(
	ax_q4, "q4", -np.pi/2,np.pi/2,
	valinit=0, valstep=0.1,
	color="green"
)

q5 = Slider(
	ax_q5, "q5", -np.pi/2,np.pi/2,
	valinit=0, valstep=0.1,
	initcolor='none'  # Remove the line marking the valinit position.
)

q6 = Slider(
	ax_q6, "q6", -np.pi/2, np.pi/2,
	valinit=0, valstep=0.1,
	initcolor='none'  # Remove the line marking the valinit position.
)
def update(val):
	ax.cla()
	l0 = 0.17
	l1 = 0.22
	l2 = 0.22
	l3 = 0.1052
	q = [q1.val, q2.val, q3.val, q4.val, q5.val, q6.val]

	teta = np.array([q[0], q[1]+np.pi/2, q[2]+np.pi/2, q[3],q[4],q[5]])
	d = np.array([l0, 0, 0, l2, 0,l3])
	a = np.array([0, l1, 0, 0, 0, 0])
	alfa = np.array([np.pi/2, 0, np.pi/2, -np.pi/2, np.pi/2, 0])



	A01 = Tdh(teta[0], d[0], a[0], alfa[0])
	A12 = Tdh(teta[1], d[1], a[1], alfa[1])
	A23 = Tdh(teta[2], d[2], a[2], alfa[2])
	A34 = Tdh(teta[3], d[3], a[3], alfa[3])
	A45 = Tdh(teta[4], d[4], a[4], alfa[4])
	A56 = Tdh(teta[5], d[5], a[5], alfa[5])
	# Matrices de transformación del primer sistema al correspondiente
	A02 = np.dot(A01, A12)
	A03 = np.dot(A02, A23)
	A04 = np.dot(A03, A34)
	A05 = np.dot(A04, A45)
	A06 = np.dot(A05, A56)
	A36 = np.dot(np.dot(A34,A45),A56)

    
	print("T36:")
	print(A36)
	print("T03:")
	print(A03)
	print("T06:")
	print(A06)
    
	pwx=  A06[0,3]-l3*A06[0,2]
	pwy = A06[1,3]-l3*A06[1,2]
	pwz=  A06[2,3]-l3*A06[2,2]

	print("pmx=",pwx, "pmy=", pwy, "pmz=", pwz)
	R=np.sqrt(pwx**2+pwy**2+(pwz-l0)**2)
	r=np.sqrt(pwx**2+pwy**2)
	print("R:", R)
	print("r:", r)

	# Vector de posicion (x, y, z) de cada sistema de coordenadas
	x0, y0, z0 = 0, 0, 0
	x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
	x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
	x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
	x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
	x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
	x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
	# Se dibuja el robot
	x = [x0, x1, x2, x3, x4, x5, x6]
	y = [y0, y1, y2, y3, y4, y5, y6]
	z = [z0, z1, z2, z3, z4, z5, z6]
	
	
	print("x = ",x6)
	print("y =",y6)
	print("z =",z6)
      
	ax.plot(x,y,z)
	ax.scatter(x, y, z)
	fig.canvas.draw_idle()
	ax.grid(True)
# Se establecen los límites de los ejes
	ax.set_xlim([-1.5, 1.5])
	ax.set_ylim([-1.5, 1.5])
	ax.set_zlim([0, 1.5])
    
	yaw, pitch, roll =obtener_angulos_euler(A06[:3, :3])
	print("yaw = np.deg2rad(",np.degrees(yaw),")")
	print("pitch = np.deg2rad(" ,np.degrees(pitch),")")
	print("roll = np.deg2rad(",np.degrees(roll),")")
	
	# Se coloca una rejilla a los ejes



	


q1.on_changed(update)
q2.on_changed(update)
q3.on_changed(update)
q4.on_changed(update)
q5.on_changed(update)
q6.on_changed(update)



plt.show()



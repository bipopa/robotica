import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
# parameters
rR = 0.075
rL = rR
b = 0.3/2
tf = 3

# initial conditions
theta0 = 0
x0 = 0
y0 = 0

# time vector and time increment
t = np.linspace(0, tf, 60)
dt = t[1] - t[0]

# initialization and pre-allocation of pose variables
x = np.zeros(len(t))
y = np.zeros(len(t))
theta = np.zeros(len(t))
theta[0] = theta0
x[0] = x0
y[0] = y0

# command signals (in RPM)
ind1 = np.where(t <= max(t)/3)[0]
ind2 = np.where((t > max(t)/3) & (t <= 2*max(t)/3))[0]
ind3 = np.where((t > 2*max(t)/3) & (t <= max(t)))[0]
vec = np.ones(len(t))
phidotR = np.concatenate((240*(2*np.pi/60)*vec[ind1], 
                          120*(2*np.pi/60)*vec[ind2], 
                          120*(2*np.pi/60)*vec[ind3]))
phidotL = np.concatenate((120*(2*np.pi/60)*vec[ind1], 
                          240*(2*np.pi/60)*vec[ind2], 
                          -120*(2*np.pi/60)*vec[ind3]))

# update loop
for ii in range(1, len(t)):
    J = np.array([[rR*np.cos(theta[ii-1])/2, rL*np.cos(theta[ii-1])/2],
                  [rR*np.sin(theta[ii-1])/2, rL*np.sin(theta[ii-1])/2],
                  [0.5*rR/b, -0.5*rL/b]])
    deltapose = dt * J @ np.array([[phidotR[ii-1]], [phidotL[ii-1]]])
    x[ii] = x[ii-1] + deltapose[0]
    y[ii] = y[ii-1] + deltapose[1]
    theta[ii] = theta[ii-1] + deltapose[2]

# plot and animation
fig1, ax1 = plt.subplots()
ax1.plot(t, phidotR, 'b', label='d(phi_R)/dt')
ax1.plot(t, phidotL, 'r', label='d(phi_L)/dt')
ax1.set_xlabel('t')
ax1.legend()
ax1.set_title('angular velocities of the wheels')

fig2, ax2 = plt.subplots()
ax2.plot(t, theta, 'b')
ax2.set_xlabel('t')
ax2.set_ylabel('theta')
ax2.set_title('angle of the robot chassis')

fig3 = plt.figure()
ax = fig3.add_subplot(111, projection='3d')
#fig3, ax = plt.subplots()
x0, y0, z0 = 0, 0, 0
p, = ax.plot([x0], [y0], [z0], 'r', linewidth=2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
    # Se asigna una rejilla a los ejes
ax.grid(True)
    # Se establecen los límites de los ejes
ax.set_xlim3d([-1, 1])
ax.set_ylim3d([-1, 1])
ax.set_zlim3d([0, 1.5])
    # Mantiene el gráfico actual


wls = np.array([[0, 0], [-0.5*b, 0.5*b]])
wlsrot = np.array([[np.cos(theta[0]), -np.sin(theta[0])], [np.sin(theta[0]), np.cos(theta[0])]]) @ wls
# Plot initialization
#fig, ax = plt.subplots()

x = [ 1, -1, -1, 1, 1]
y = [ 1, 1, -1, -1, 1]
xx = [ 0, 0, 0, 0, 0]
yy = [ 0, 0, 0, 0, 0]
z = [ 0, 0, 0, 0, 0]
zz = [1, 1, 1, 1, 1]
theta=[0, 0.5, 1.0 ,1.5, 2]
p.set_data(x, y)
p.set_3d_properties(z)
# Update loop
for ii in range(5):
    wlsrot = np.array([[np.cos(theta[ii]), -np.sin(theta[ii])],
                       [np.sin(theta[ii]), np.cos(theta[ii])]]) @ [x,y]#wls
    h1x=(wlsrot[0,0] + xx[ii])
    h1y=(wlsrot[1,0] + yy[ii])
    h2x=(wlsrot[0,1] + xx[ii])
    h2y=(wlsrot[1,1] + yy[ii])
    h3x=(wlsrot[0,2] + xx[ii])
    h3y=(wlsrot[1,2] + yy[ii])
    h4x=(wlsrot[0,3] + xx[ii])
    h4y=(wlsrot[1,3] + yy[ii])
    h5x=(wlsrot[0,4] + xx[ii])
    h5y=(wlsrot[1,4] + yy[ii])
    #print([h1x,h2x, h3x,h4x,h5x], [h1y,h2y,h3y,h4y,h5y])
    p.set_data([h1x,h2x, h3x,h4x,h5x], [h1y,h2y,h3y,h4y,h5y])
    p.set_3d_properties(zz)
    plt.ion()
    plt.show()
    plt.pause(1)

plt.draw()
print(wlsrot)
plt.show()
""" while True:
    time.sleep(1) """
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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
fig3, ax = plt.subplots()
ax.plot(x, y, 'k--')
ax.set_title('workspace')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xlim(-1.25, 1.25)
ax.set_ylim(-0.5, 2)
wls = np.array([[0, 0], [-0.5*b, 0.5*b]])
wlsrot = np.array([[np.cos(theta[0]), -np.sin(theta[0])], [np.sin(theta[0]), np.cos(theta[0])]]) @ wls
# Plot initialization
#fig, ax = plt.subplots()
h1, = ax.plot(wlsrot[0,0]+x[0], wlsrot[1,0]+y[0], 'ro', linewidth=2, markersize=6, markerfacecolor='r')
h2, = ax.plot(wlsrot[0,1]+x[0], wlsrot[1,1]+y[0], 'ro', linewidth=2, markersize=6, markerfacecolor='r')
h3, = ax.plot(x[0], y[0], 'bo', markersize=20)
# Update loop
for ii in range(1, len(t)):
 wlsrot = np.array([[np.cos(theta[ii]), -np.sin(theta[ii])],
[np.sin(theta[ii]), np.cos(theta[ii])]]) @ wls
 h1.set_xdata(wlsrot[0,0] + x[ii])
 h1.set_ydata(wlsrot[1,0] + y[ii])
 h2.set_xdata(wlsrot[0,1] + x[ii])
 h2.set_ydata(wlsrot[1,1] + y[ii])
 h3.set_xdata(x[ii])
 h3.set_ydata(y[ii])
 plt.ion()
 plt.show()
 plt.pause(.1)
plt.draw()
plt.show()

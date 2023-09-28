import numpy as np
from denavit import denavit
# Define Denavit-Hartenberg parameters
teta = np.pi/4  # joint angle in radians
d = 0.5  # joint offset
a = 0.3  # link length
alfa = np.pi/2  # link twist in radians

# Calculate homogeneous transformation matrix
dh = denavit(teta, d, a, alfa)

# Print the resulting transformation matrix
print("Homogeneous transformation matrix:")
print(dh)

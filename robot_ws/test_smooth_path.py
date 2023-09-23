import numpy as np
import matplotlib.pyplot as plt
from smooth_curves import smooth_curves
from smooth_curves_three_terms import smooth_curves_three_terms
def test_smooth_paths():
    mu = 0.055
    eta = 0.010
    N = 300
    epsilon = 0.00001
    p = np.array([[0.0, 0.0], [1.0, 0.0], [1.7075, 0.7075], [2.7075, 0.7075], [2.7075, 1.7075], [1.9575, 1.7075], [2.9575, 2.4150]])
    s, z = smooth_curves(p, mu, eta, N, epsilon)

    # Plot original and smooth path
    plt.figure(figsize=(12, 4))
    #plt.figure()
    plt.subplot(1, 2, 1)
    plt.plot(p[:,0], p[:,1], 'ro-', s[:,0], s[:,1], 'bx-')
    #plt.show()

    # Plot log(z)
    #plt.figure()
    #plt.plot(np.log(z))
    #plt.show()

    s_T, z_T = smooth_curves_three_terms(p, mu, eta, N, epsilon)

    # Plot original and smooth path
    #plt.figure()
    plt.subplot(1, 2, 2)
    plt.plot(p[:,0], p[:,1], 'ro-', s_T[:,0], s_T[:,1], 'bx-')
    plt.show()

    # Plot log(z)
    #plt.figure()
    #plt.plot(np.log(z_T))
    #plt.show()
test_smooth_paths()
import numpy as np

def smooth_curves(p, mu, eta, N, epsilon):
    # This function smooths a path
    # p = (x,y) original path points
    # s = (x,y) smooth path
    # mu = step-size for p and s
    # eta = step-size for s
    # epsilon = limit to stop the algorithm

    size_p = p.shape
    sP = size_p[0]
    s = np.zeros(size_p)
    st = np.zeros(size_p)
    # Z = np.zeros(N)
    # Z_previous = 0
    z_previous = 0

    for n in range(N):
        st[0:sP-1,:] = s[1:sP,:]
        s = s + mu * (p - s) + eta * (st - s)
        dif_ps = p - s
        dif_ss = st - s
        z = np.dot(dif_ps.T, dif_ps) + np.dot(dif_ss.T, dif_ss)
        zz = z[0] + z[1]
        dif_z = np.sqrt(abs((zz - z_previous) * (zz - z_previous)))
        z_previous = zz
        # Z[n] = dif_z

        # pause
        #if dif_z(1) < epsilon:
         #  break

    s[0,:] = p[0,:]
    s[sP-1,:] = p[sP-1,:]
    # n
    # Z[n]
    return s, z

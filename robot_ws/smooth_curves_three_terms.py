import numpy as np

def smooth_curves_three_terms(p, mu, eta, N, epsilon):
    size_p = p.shape
    sP = size_p[0]
    s = np.zeros(size_p)
    st = np.zeros(size_p)
    stm = np.zeros(size_p)
    z_previous = 0
    Z = np.zeros(N)

    for n in range(N):
        st[0:sP-1, :] = s[1:sP, :]
        stm[1:sP, :] = s[0:sP-1, :]
        s = s + mu * (p - s) + eta * (stm - 2 * s + st)
        dif_ps = p - s
        dif_ss = st - s
        dif_sm = stm - s
        z = np.dot(dif_ps.T, dif_ps) + np.dot(dif_ss.T, dif_ss) + np.dot(dif_sm.T, dif_sm)
        zz = z[0] + z[1]
        dif_z = np.sqrt(abs((zz - z_previous) * (zz - z_previous)))
        z_previous = zz
        #Z[n] = dif_z

       # if dif_z < epsilon:
        #    break

    s[0, :] = p[0, :]
    s[sP-1, :] = p[sP-1, :]
    return s, Z[n]

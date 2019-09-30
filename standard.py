import numpy as np

def atmosphere(alt):
    #Constants
    REARTH = 6369.0 #radius of earth
    GMR = 34.163195 #hydrostatic constant
    NTAB = 8 #number of entries in defining tables

    #Define defining tables
    htab = [0.0, 11.0, 20.0, 32.0, 47.0, 51.0, 71.0, 84.852]
    ttab = [288.15, 216.65, 216.65, 228.65, 270.65, 270.65, 214.65, 186.946]
    ptab = [1.0, 2.233611E-1, 5.403295E-2, 8.5666784E-3, 1.0945601E-3, 6.6063531E-4, 3.9046834E-5, 3.68501E-6]
    gtab = [-6.5, 0.0, 1.0, 2.8, 0.0, -2.8, -2.0, 0.0]

    #Calculate
    h = alt*REARTH/(alt+REARTH) #convert to geopotential alt
    i = 1
    j = NTAB

    while(j > i+1):
        k = int((i+j)/2) #integer division
        if(h < htab[k]):
            j=k
        else:
            i=k
    tgrad = gtab[i]
    tbase = ttab[i]
    deltah = h-htab[i]
    tlocal = tbase + tgrad * deltah
    theta = tlocal/ttab[0]

    if(tgrad == 0.0):
        delta = ptab[i] * np.exp(-1*GMR*deltah/tbase)
    else:
        delta = ptab[i] * (tbase/tlocal)**(GMR/tgrad)

    sigma = delta/theta
    return sigma, delta, theta

def get_standard_atmosphere_1d(z):
    NZ = z.shape[0]
    p0 = 1.013250e5
    t0 = 288.15
    p = np.zeros(z.shape)
    t = np.zeros(z.shape)

    for i in np.arange(NZ):
        sigma, delta, theta = atmosphere(z[i]/1000.) #convert to km
        p[i] = p0 * delta
        t[i] = t0 * theta
    return p, t

def get_standard_atmosphere_2d(z):
    NZ = z.shape[1]
    NY = z.shape[0]
    p0 = 1.013250e5
    t0 = 288.15
    p = np.zeros(z.shape)
    t = np.zeros(z.shape)

    for i in np.arange(NY):
        for j in np.arange(NZ):
            sigma, delta, theta = atmosphere(z[i,j]/1000.) #convert to km
            p[i,j] = p0 * delta
            t[i,j] = t0 * theta
    return p, t

def get_standard_atmosphere_3d(z):
    NZ = z.shape[2]
    NX = z.shape[0]
    NY = z.shape[1]
    p0 = 1.013250e5
    t0 = 288.15
    p = np.zeros(z.shape)
    t = np.zeros(z.shape)

    for i in np.arange(NX):
        for j in np.arange(NY):
            for k in np.arange(NZ):
                sigma, delta, theta = atmosphere(z[i,j,k]/1000.) #convert to km
                p[i,j,k] = p0 * delta
                t[i,j,k] = t0 * theta
    return p, t

import math
import numpy as np
from Rod2Axan import Rod2Axan
def Rod2Ho(rho,Rho):
    n = (Rod2Axan(rho,Rho))[0]
    w = math.radians((Rod2Axan(rho,Rho))[1])
    if Rho == 0:
        h = [0,0,0]
    elif Rho == math.inf:
        h = np.zeros(len(n))
        f = (3*(math.pi))/(4)
        for i in range(0,3):
            h[i] = n[i]*f
    else:
        f = (3)*(w-math.sin(w))*(0.25)
        h = np.zeros(len(n))
        for i in range(0,len(n)):
            h[i] = n[i]*f
    return h
rho = [0, -0, -1]
Rho = 1
print(Rod2Ho(rho,Rho))
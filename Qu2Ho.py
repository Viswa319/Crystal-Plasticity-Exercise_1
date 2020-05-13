import math
import numpy as np
from modulus import modulus
def Qu2Ho(q):
    w = 2*math.acos(q[0])
    h = np.zeros(3)
    if w == 0:
        return h 
    else:
        s = 1/modulus((q[1:4]))
        n = np.zeros(3)
        f = 3*(w - math.sin(w))/4
        for i in range(0,len(n)):
            n[i] = s*q[i+1]
            h[i]  = n[i]*(f**(1/3))
        return h
q = [0,0,0,1]
print(Qu2Ho(q))
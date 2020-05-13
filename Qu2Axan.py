import math
import numpy as np
from permutation_tensor import sgn
from modulus import modulus
def Qu2Axan(q):
    w = round(2*math.acos(q[0]),5)
    if w == 0:
        n = [0,0,1]
        return n,w
    else:
        if q[0] == 0:
            n = [q[1],q[2],q[3]]
            w = math.degrees(math.pi)
            return n,w 
        else:
            s = sgn(q[0])/(modulus(q[1:4]))
            n = np.zeros(3)
            for i in range(0,len(n)):
                n[i] = s*q[i+1]
            return n,round(math.degrees(w))
q = [0.7071068 ,0.0000000, 0.0000000, 0.7071068] 
print(Qu2Axan(q))
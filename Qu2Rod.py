import math
import numpy as np
from modulus import modulus 
def Qu2Rod(q):
    s = modulus(q[1:4])
    t = math.tan(math.acos(q[0]))
    rho = np.zeros(3)
    for i in range(0,len(rho)):
        rho[i] = q[i+1]/s
        Rho = round(t)
    return rho,Rho
q = [0.7071068, 0.0000000, 0.0000000, 0.7071068]
print(Qu2Rod(q))
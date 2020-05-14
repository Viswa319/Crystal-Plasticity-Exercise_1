import math
import numpy as np
from modulus import modulus 
#This function transforms quarternions to homochoric representation
def Qu2Rod(q):
    rho = np.zeros((len(q),4))
    s = np.zeros(len(q))
    t = np.zeros(len(q))
    for j in range(0,len(q)):
        s[j] = modulus(q[j][1:4])
        t[j] = math.tan(math.acos(q[j][0]))
        if s[j] != 0:
            for i in range(0,3):
                rho[j][i] = q[j][i+1]/s[j]
                rho[j][3] = round(t[j])
        else:
            rho[j][0:3] = [0,0,-1]
    return rho
# Testing the function for few values
q = [[1.0000000, 0.0000000, 0.0000000, 0.0000000],[0.7071068 ,0.0000000, 0.0000000, 0.7071068],[0.0000000 ,0.0000000, 0.0000000, 1.0000000]]
print(Qu2Rod(q))
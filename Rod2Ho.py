import math
import numpy as np
from Rod2Axan import Rod2Axan
#This function transforms from Rodrigues representation to homochoric representation
def Rod2Ho(rho):
    n = np.zeros((len(rho),4))
    w = np.zeros(len(rho))
    h = np.zeros((len(rho),3))
    f = np.zeros(len(rho))
    for i in range(0,len(rho)):
        n[i] = (Rod2Axan(rho))[i] #first transforming Rodrigues representation to axis angle pair
        if rho[i][3] == 0: #this is for the case where angle of rotation is 0
            h[i] = [0,0,0]
        elif rho[i][3] == math.inf: #this is for the case where angle of rotation is pi
            f[i] = (3*(math.pi))/(4)
            for j in range(0,3):
                h[i][j] = n[i][j]*f[i]
        else:
            w[i] = math.radians(n[i][3])
            f[i] = (3)*(w[i]-math.sin(w[i]))*(0.25)
            for j in range(0,3):
                h[i][j] = (n[i][j])*(f[i]**(1/3)) 
    return h
# Testing the function for few values
#Input array of Rodrigues vector/vectors of size (n,4) where n will be the number of Rodrigues vectors
rho = [[0.0000000, 0.0000000, -1.0000000, 0.0000000],[0.0000000, 0.0000000, 1.0000000, 1.0000000]]
print(Rod2Ho(rho))
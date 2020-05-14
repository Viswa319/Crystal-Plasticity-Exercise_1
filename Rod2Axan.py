import math
import numpy as np
from modulus import modulus, normalize
#This function transforms from Rodrigues representation to axis angle pair
def Rod2Axan(rho):
    n = np.zeros((len(rho),4))
    for i in range(0,len(rho)):
        n[i][0:3] = normalize(rho[i][0:3])
        n[i][3] = round(math.degrees(2*(math.atan(rho[i][3]))),5)
    return n
# Testing the function for few values
#Input array of Rodrigues vector/vectors of size (n,4) where n will be the number of Rodrigues vectors
rho = [[0.0000000, 0.0000000, -1.0000000, 0.0000000],[0.0000000, 0.0000000, 1.0000000, 1.0000000]]
print(Rod2Axan(rho))


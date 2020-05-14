import numpy as np
import math
from permutation_tensor import permutation
#This function transforms from rotation matrix to Rodrigues representation
def Rot2Rod(A):
    rho = np.zeros((len(A),4)) #Creating an arrays with zeros in it
    tr = np.zeros(len(A))
    x = np.zeros(len(A))
    for S in range(0,len(A)):
        for t in range(0,3):
            tr[S] = tr[S] + A[S][t][t]
            x[S] = math.acos((0.5)*(tr[S]-1)) #Calculating angle of rotation
        if x[S] == 0: #if angle of rotation is 0
            rho[S][0:3] = [0,0,-1] #Assigning Rodrigues vector
        else:    
            for k in range(0,3):
                for i in range(0,3):
                    for j in range(0,3):
                        rho[S][k] = rho[S][k] + ((permutation(k,i,j))*(A[S][i][j]))*((1+tr[S])**(-1)) #Assigning Rodrigues vector
        rho[S][3] = math.tan(x[S]*0.5)
    return rho
#Testing function for few values
#Input array of rotation matrix/matrices of size (n,3,3) where n will be the number of rotation matrices
A = [[[1,0,0],[0,1,0],[0,0,1]],[[0,1,0],[-1,0,0],[0,0,1]]]
print(Rot2Rod(A))
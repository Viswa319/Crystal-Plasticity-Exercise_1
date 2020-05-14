import math
import numpy as np
from permutation_tensor import permutation
from modulus import normalize,modulus
#This function transforms from rotation matrix to axis angle representation
def Rot2Axa(A):
    tr = np.zeros(len(A))
    x = np.zeros(len(A))
    R = np.zeros((len(A),4))
    for L in range(0,len(A)):
        tr[L] = 0
        for k in range(0,len(A[L])): 
            tr[L] = tr[L] + A[L][k][k] #rotation angle depends on the trace of a matrix 
            x[L] = math.degrees(math.acos((0.5)*(tr[L]-1)))
            if x[L] == 0: #This is for the special case if rotation angle is zero
                R[L] = [0,0,1,x[L]]
            else:
                for i in range(0,3): #Axis vector depends on the off diagonal terms
                    for j in range(0,3):
                        R[L][k] = R[L][k] + permutation(k,i,j)*A[L][i][j]
                        R[L][3] = x[L]
        if np.size(R) !=4: #This normalizes the axis vector if the modulus of vector is not equal to zero 
            if modulus(R[L][0:3])!=0:
                R[L][0:3] = normalize(R[L][0:3])
                R[L][3] = x[L]
        else:
            if modulus(R[0:3])!=0:
                R[0:3] = normalize(R[0:3])
                R[3] = x[L]
    return R,tr
#Testing function for few values
#Input array of rotation matrix/matrices of size (n,3,3) where n will be the number of rotation matrices
A = [[[1,0,0],[0,1,0],[0,0,1]],[[0,1,0],[-1,0,0],[0,0,1]]]
print(Rot2Axa(A))
print(len(A))
import math
import numpy as np
from permutation_tensor import permutation
#This function transforms quarternions to rotation matrix
def Qu2Rot(q):
    q1  = np.zeros(len(q))
    Q = np.zeros((len(q),3))
    A = np.zeros((len(q),3,3))
    for S in range(0,len(q)):
        q1[S] = (q[S][0]**2)-((q[S][1]**2)+(q[S][2]**2)+(q[S][3]**2))
        Q[S]  = q[S][1:4]
        P = -1
        for i in range(0,3):
            A[S][i][i] = round(q1[S] + 2*(Q[S][i])**2,5)
            for j in range(0,3):
                for k in range(0,3):
                    if i != j and i!=k and j!=k:  
                        A[S][i][j] = round(2*((Q[S][i])*(Q[S][j])-P*permutation(i,j,k)*q[S][0]*Q[S][k]),5)
    return A
# Testing the function for few values
#Input array of quarternions of size (n,4) where n will be the number of set of quarternions 
q = [[1.0000000, 0.0000000, 0.0000000, 0.0000000],[0.7071068 ,0.0000000, 0.0000000, 0.7071068],[0.0000000 ,0.0000000, 0.0000000, 1.0000000]]
print(Qu2Rot(q))
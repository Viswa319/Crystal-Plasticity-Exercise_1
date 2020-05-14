import numpy as np
from modulus import normalize
from modulus import modulus
#This function transforms from rotation matrix to quarternions
def Rot2Qu(A):
    Q = np.zeros((len(A),4))
    for i in range(0,len(A)):
        P = -1
        Q[i][0] = 0.5*np.sqrt(1+A[i][0][0]+A[i][1][1]+A[i][2][2]) #Transforming rotation matrix to quarternions each term individually
        Q[i][1] = P*0.5*np.sqrt(1+A[i][0][0]-A[i][1][1]-A[i][2][2])
        Q[i][2] = P*0.5*np.sqrt(1-A[i][0][0]+A[i][1][1]-A[i][2][2])
        Q[i][3] = P*0.5*np.sqrt(1-A[i][0][0]-A[i][1][1]+A[i][2][2])
        if A[i][2][1] < A[i][1][2]:
            Q[i][1] = -1*Q[i][1]
        if A[i][0][2] < A[i][2][0]:
            Q[i][2] = -1*Q[i][2]
        if A[i][1][0] < A[i][0][1]:
            Q[i][3] = -1*Q[i][3]
        if modulus(Q[i][0:4]) !=0: #Normalizing quarternions
            Q[i][0:4] = normalize(Q[i][0:4])
    return Q
#Testing function for few values
#Input array of rotation matrix/matrices of size (n,3,3) where n will be the number of rotation matrices
A = [[[1,0,0],[0,1,0],[0,0,1]],[[0,1,0],[-1,0,0],[0,0,1]]]
print(Rot2Qu(A))

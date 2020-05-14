import math
import numpy as np
#This function transforms from rotation matrix to axis angle representation
def Rot2Eul(A):
    X = np.zeros((len(A),3)) #Creating vectors with zeros in it
    x = np.zeros((len(A),3))
    for i in range(0,len(A)):
        if A[i][2][2] == 1: #if the last diagonal element of rotation tensor is 1 
            X[i][1] = 0
            X[i][0] = math.atan2(A[i][0][1],A[i][0][0])
            X[i][2] = X[i][0]
        else: # Transforming rotation matrix to Euler angles
            X[i][1] = math.acos(A[i][2][2]) 
            X[i][0] = math.atan2((A[i][2][0]/math.sin(X[i][1])),-(A[i][2][1]/math.sin(X[i][1])))
            X[i][2] = math.atan2((A[i][0][2]/math.sin(X[i][1])),(A[i][1][2]/math.sin(X[i][1])))
        x[i][0] = math.degrees(X[i][0]) #Converting from radians to degrees
        x[i][1] = math.degrees(X[i][1])
        x[i][2] = math.degrees(X[i][2])
    return x
#Testing function for few values
#Input array of rotation matrix/matrices of size (n,3,3) where n will be the number of rotation matrices
A = [[[1,0,0],[0,1,0],[0,0,1]],[[0,1,0],[-1,0,0],[0,0,1]]]
print(Rot2Eul(A))

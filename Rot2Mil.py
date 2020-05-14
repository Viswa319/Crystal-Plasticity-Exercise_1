import numpy as np
#This function transforms from rotation matrix to miller indices
def Rot2Mil(A):
    b = np.zeros((len(A),2,3)) #Creating an array with zeros in it
    for j in range(0,len(A)):
        for i in range(0,3):
            b[j][0][i] = A[j][i][0] #Assigning direction miller indices
            b[j][1][i] = A[j][i][1] #Assigning plane miller indices
    return b
#Testing function for few values
#Input array of rotation matrix/matrices of size (n,3,3) where n will be the number of rotation matrices
A = [[[1,0,0],[0,1,0],[0,0,1]],[[0,1,0],[1,0,0],[0,0,1]]]
print(Rot2Mil(A))
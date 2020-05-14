import math
import numpy as np
from permutation_tensor import permutation
#This function transforms from axis angle pair to rotation matrix
def Axan2Rot(N):
    A = np.zeros((len(N),3,3)) #Creating array with zeros in it
    for s in range(0,len(N)):
        W = math.radians(N[s][3]) #This converts angle from degrees to radians
        co = math.cos(W) 
        si = math.sin(W)
        for i in range(0,3):
            A[s][i][i] = co + (1-co)*(N[s][i])**2 #Modifying diagonal values of rotation matrix with appropriate formulae
            for j in range(0,3):
                for k in range(0,3):
                    if i != j and i!=k and j!=k:
                        A[s][i][j] = round((1-co)*(N[s][i])*(N[s][j])+permutation(i,j,k)*si*N[s][k]) #Modifying non-diagonal values of rotation matrix with appropriate formulae
    return A
# Testing the function for few values
#This function takes input as axis angle pair of size (n,4) where n is the number of sets of axis angle pair vectors
N = [[0,0,1,0],[0,0,1,90],[0,0,1,180]]
print(Axan2Rot(N))
import math
import numpy as np
from permutation_tensor import permutation
from modulus import normalize,modulus
def Rot2Axa(A):
    R = np.zeros(len(A))
    tr = 0
    for k in range(0,len(A)):
        tr = tr + A[k][k]
        X = math.acos((0.5)*(tr-1))
        x = math.degrees(X)
        if x == 0:
            R = [0,0,1]
        else:
            for i in range(0,len(A)):
                for j in range(0,len(A)):
                    R[k] = R[k] + permutation(k,i,j)*A[i][j]
    if modulus(R)!=0:
        r = normalize(R)
    return r,X

A = [[ 1, 0, 0],
 [0 , 1,  0],
 [ 0 , 0, 1]]
print(Rot2Axa(A))
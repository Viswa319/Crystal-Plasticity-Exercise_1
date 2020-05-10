import numpy as np
from permutation_tensor import permutation
def rot2rod(A):
    tr = 0
    for i in range(0,len(A)):
        tr = tr + A[i][i]
    rho = np.zeros(len(A))
    for k in range(0,len(A)):
        for i in range(0,len(A)):
            for j in range(0,len(A)):
                rho[k] = rho[k] + (permutation(k,i,j)*A[i][j])*((1+tr)**(-1))
    return rho
A = [[ 1, 0, 0],
 [0 , 0,  1],
 [ 0 , -1 , 0]]
print(rot2rod(A))
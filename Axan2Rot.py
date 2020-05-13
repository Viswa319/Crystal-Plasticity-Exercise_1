import math
import numpy as np
from permutation_tensor import permutation
def Axan2Rot(n,w):
    W = math.radians(w)
    c = math.cos(W)
    s = math.sin(W)
    A = np.zeros((3,3))
    for i in range(0,3):
        A[i][i] = c + (1-c)*(n[i])**2
        for j in range(0,3):
            for k in range(0,3):
                if i != j and i!=k and j!=k:
                    A[i][j] = (1-c)*(n[i])*(n[j])+permutation(i,j,k)*s*n[k]
    return A
n = [0,0,1]
w = 0
print(Axan2Rot(n,w))
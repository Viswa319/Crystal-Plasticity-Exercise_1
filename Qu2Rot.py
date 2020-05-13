import math
import numpy as np
from permutation_tensor import permutation
def Qu2Rot(q):
    q1 = (q[0]**2)-((q[1]**2)+(q[2]**2)+(q[3]**2))
    Q  = q[1:4]
    A = np.zeros((3,3))
    P = -1
    for i in range(0,3):
        A[i][i] = round(q1 + 2*(Q[i])**2,5)
        for j in range(0,3):
            for k in range(0,3):
                if i != j and i!=k and j!=k:  
                    A[i][j] = round(2*((Q[i])*(Q[j])-P*permutation(i,j,k)*q[0]*Q[k]),5)
    return A
q = [0.7071068, 0.0000000, 0.0000000, 0.7071068]
print(Qu2Rot(q))
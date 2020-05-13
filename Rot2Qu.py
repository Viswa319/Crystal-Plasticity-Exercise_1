import numpy as np
from modulus import normalize
from modulus import modulus
def Rot2Qu(A):
    P = -1
    Q = np.zeros(4)
    Q[0] = 0.5*np.sqrt(1+A[0][0]+A[1][1]+A[2][2])
    Q[1] = P*0.5*np.sqrt(1+A[0][0]-A[1][1]-A[2][2])
    Q[2] = P*0.5*np.sqrt(1-A[0][0]+A[1][1]-A[2][2])
    Q[3] = P*0.5*np.sqrt(1-A[0][0]-A[1][1]+A[2][2])
    if A[2][1] < A[1][2]:
        Q[1] = -1*Q[1]
    if A[0][2] < A[2][0]:
        Q[2] = -1*Q[2]
    if A[1][0] < A[0][1]:
        Q[3] = -1*Q[3]  
    if modulus(Q[1:4]) !=0:  
        Q[1:4] = normalize(Q[1:4])
    return Q
A = [[1 ,0, 0], [0,1,0],[0,0,1]]
print(Rot2Qu(A))

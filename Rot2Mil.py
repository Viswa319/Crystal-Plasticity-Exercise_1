import numpy as np
def Rot2Mil(A):
    b = np.zeros(len(A))
    n = np.zeros(len(A))
    for i in range(0,len(b)):
            b[i] = A[i][0]
            n[i] = A[i][2]
    return b,n
A = [[1 ,0, 0], [0,0,1],[0,-1,0]]
print(Rot2Mil(A))
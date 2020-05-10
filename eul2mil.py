import math
import numpy as np
def eul2mil(x,y,z):
    b = np.zeros(3)
    n = np.zeros(3)
    X = math.radians(x)
    Y = math.radians(y)
    Z = math.radians(z)
    b[0] = np.round((np.cos(X)*np.cos(Z)) -(np.sin(X)*np.sin(Z)*np.cos(Y)),3)
    b[1] = np.round(-(np.cos(X)*np.sin(Z)) -(np.sin(X)*np.cos(Z)*np.cos(Y)),3)
    b[2] = np.round(np.sin(X)*np.sin(Y),3)
    S = 1
    while True:
        B = np.dot(b,S)
        S = S+1
        if B[0]%1 == 0 and B[1]%1 ==0 and B[2]%1 ==0:
            break
    n[0] = np.sin(Y)*np.sin(Z)
    n[1] = np.sin(Y)*np.cos(Z)
    n[2] = np.cos(Y)
    T = 1
    while True:
        N = np.dot(n,T)
        T = T+1
        if N[0]%1 == 0 and N[1]%1 ==0 and N[2]%1 ==0:
            break
    return B,N
print(eul2mil(90,0,0))

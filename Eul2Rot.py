import numpy as np
import math
def Rotation_Tensor(k1,x):
    X = math.radians(x)
    Z1 = np.zeros((3,3))
    for i in range(0,3):
        for j in range(0,3):
            Z1[k1,k1] = 1
            if i == j and i!=k1 and j!=k1:
                Z1[i,j] = round(math.cos(X),7)
            elif i != j and i < j and i!=k1 and j!=k1:
                Z1[i,j] = round(math.sin(X),7)
            elif i != j and i > j and i!=k1 and j!=k1:
                Z1[i,j] = -round(math.sin(X),7)
    return Z1
def Eul2Rot(k1,x,k2,y,k3,z):
    Z1 = Rotation_Tensor(k1,x)
    X = Rotation_Tensor(k2,y)
    Z2 = Rotation_Tensor(k3,z)
    Y = np.dot(Z2,X)
    R = np.dot(Y,Z1)
    return R
print(Eul2Rot(2,360,0,0,2,360))

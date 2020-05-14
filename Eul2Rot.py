import numpy as np
import math
#This function takes input of angle and rotation about given axis and generates a direction cosine matrix(rotation matrix)
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
#This function transforms Euler angles  to rotation matrix
def Eul2Rot(Theta,rotation):
    Z1 = np.zeros((len(Theta),3,3))
    Z2 = np.zeros((len(Theta),3,3))
    X = np.zeros((len(Theta),3,3))
    Y = np.zeros((len(Theta),3,3))
    R = np.zeros((len(Theta),3,3))    
    for i in range(0,len(Theta)):
        Z1[i] = Rotation_Tensor(rotation[i][0],Theta[i][0]) #Generates a direction cosine matrix for first rotation
        X[i] = Rotation_Tensor(rotation[i][1],Theta[i][1]) #Generates a direction cosine matrix for second rotation
        Z2[i] = Rotation_Tensor(rotation[i][2],Theta[i][2]) #Generates a direction cosine matrix for third rotation
        Y[i] = np.dot(Z2[i],X[i]) #Multiplies third and second rotation matrices
        R[i] = np.dot(Y[i],Z1[i]) #Multiplies the resultant matrix from above operation and first rotation matrix which gives the final rotation
    return R
# Testing the function for few values
Theta = [[0,0,0],[90,0,0],[90,360,-90]]
rot = [[2,0,2],[2,0,2],[2,0,2]]
print(Eul2Rot(Theta,rot))

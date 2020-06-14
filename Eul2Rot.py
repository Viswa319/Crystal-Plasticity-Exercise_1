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
def Eul2Rot(Theta):#This function takes input of vector of Euler indices of size (n,3) and 
    #set of rotations (for example (3,1,3)) of size (n,3) where n is the number of sets of euler angles
    Z1 = np.zeros((len(Theta),3,3))
    Z2 = np.zeros((len(Theta),3,3))
    X = np.zeros((len(Theta),3,3))
    Y = np.zeros((len(Theta),3,3))
    R = np.zeros((len(Theta),3,3))    
    for i in range(0,len(Theta)):
        Z1[i] = Rotation_Tensor(2,Theta[i][0]) #Generates a direction cosine matrix for first rotation
        X[i] = Rotation_Tensor(0,Theta[i][1]) #Generates a direction cosine matrix for second rotation
        Z2[i] = Rotation_Tensor(2,Theta[i][2]) #Generates a direction cosine matrix for third rotation
        Y[i] = np.dot(Z2[i],X[i]) #Multiplies third and second rotation matrices
        R[i] = np.dot(Y[i],Z1[i]) #Multiplies the resultant matrix from above operation and first rotation matrix which gives the final rotation
    return R
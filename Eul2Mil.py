import math
import numpy as np
#This function transforms Euler angles  to Miller indices
def Eul2Mil(Theta):
    b = np.zeros((len(Theta),3)) #Creating array with zeros in it
    n = np.zeros((len(Theta),3)) #Creating array with zeros in it
    for i in range(0,len(Theta)):
        X = math.radians(Theta[i][0]) #This converts first Euler angle from degrees to radians
        Y = math.radians(Theta[i][1]) #This converts second Euler angle from degrees to radians
        Z = math.radians(Theta[i][2]) #This converts third Euler angle from degrees to radians
        b[i][0] = np.round((np.cos(X)*np.cos(Z)) -(np.sin(X)*np.sin(Z)*np.cos(Y)),3) #Assigning first term of direction Miller indices
        b[i][1] = np.round(-(np.cos(X)*np.sin(Z)) -(np.sin(X)*np.cos(Z)*np.cos(Y)),3) #Assigning second term of direction Miller indices
        b[i][2] = np.round(np.sin(X)*np.sin(Y),3) #Assigning third term of direction Miller indices
        #S = 1
        #while True:
        #    B[i] = np.dot(b[i],S)
        #    S = S+1
        #    if B[i][0]%1 == 0 and B[i][1]%1 ==0 and B[i][2]%1 ==0:
        #        break
        n[i][0] = np.round(np.sin(Y)*np.sin(Z),3) #Assigning first term of plane Miller indices
        n[i][1] = np.round(np.sin(Y)*np.cos(Z),3) #Assigning second term of plane Miller indices
        n[i][2] = np.round(np.cos(Y),3) #Assigning third term of plane Miller indices
        #T = 1
        #while True:
        #    N[i] = np.dot(n[i],T)
        #    T = T+1
        #    if N[i][0]%1 == 0 and N[i][1]%1 ==0 and N[i][2]%1 ==0:
        #        break
    return b,n
# Testing the function for few values
Theta = [[0,90,90],[90,0,0],[180,0,0]]
print(Eul2Mil(Theta))
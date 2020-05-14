import math
import numpy as np
#This function transforms Euler angles  to quarternions
def Eul2Qu(Theta):
    q = np.zeros((len(Theta),4))
    for i in range(0,len(Theta)):
        X = math.radians(Theta[i][0]) #This converts first Euler angle from degrees to radians
        Y = math.radians(Theta[i][1]) #This converts second Euler angle from degrees to radians
        Z = math.radians(Theta[i][2]) #This converts third Euler angle from degrees to radians
        sigma = 0.5*(X+Z)
        delta = 0.5*(X-Z)
        c = math.cos(Y*0.5)
        s = math.sin(Y*0.5)
        P = -1
        q[i][0] = round(c*math.cos(sigma),7) #Assigning first term of quarternions
        q[i][1] = round(-P*s*math.cos(delta),7) #Assigning second term of quarternions
        q[i][2] = round(-P*s*math.sin(delta),7) #Assigning third term of quarternions
        q[i][3] = round(-P*c*math.sin(sigma),7) #Assigning fourth term of quarternions
    return q
# Testing the function for few values
#This function takes input of vector of Euler indices of size (n,3) where n is the number of sets of euler angles
Theta = [[0,0,0],[90,0,0],[180,0,0]]
print(Eul2Qu(Theta))
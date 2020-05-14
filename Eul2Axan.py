import numpy as np
import math
#This function transforms Euler angles  to axis angle pair representation
def Eul2Axa(Theta):
    n = np.zeros((len(Theta),4)) #Creating array with zeros in it
    for i in range(0,len(Theta)):
        X = math.radians(Theta[i][0]) #This converts first Euler angle from degrees to radians
        Y = math.radians(Theta[i][1]) #This converts second Euler angle from degrees to radians
        Z = math.radians(Theta[i][2]) #This converts third Euler angle from degrees to radians
        t = math.tan(Y/2)
        sigma = (0.5)*(X+Z)
        delta = (0.5)*(X-Z)
        tau = math.sqrt((t**2)+(math.sin(sigma))**2)
        alpha = 2*(math.atan2(tau,math.cos(sigma)))
        P = -1
        if round(alpha,6) == 0: #This is for the special case if rotation angle is equal to 0
            n[i][0] = 0
            n[i][1] = 0
            n[i][2] = 1
            n[i][3] = 0 
        elif alpha <= math.pi: #This is for alpha less than or equal to pi
            n[i][0] = np.round(-P*t*((tau)**(-1))*(math.cos(delta)),6)
            n[i][1] = np.round(-P*t*((tau)**(-1))*(math.sin(delta)),6)
            n[i][2] = np.round(-P*((tau)**(-1))*(math.sin(sigma)),6)
            n[i][3]= np.round(math.degrees(alpha),6)
        elif alpha > math.pi : #This is for alpha greater than or equal to pi
            n[i][0] = np.round(P*t*((tau)**(-1))*(math.cos(delta)),6)
            n[i][1] = np.round(P*t*((tau)**(-1))*(math.sin(delta)),6)
            n[i][2] = np.round(P*((tau)**(-1))*(math.sin(sigma)),6)
            n[i][3] =  np.round(math.degrees((2*math.pi)-alpha),6)
    return(n)
# Testing the function for few values
Theta = [[0,0,0],[90,0,0],[180,0,0]]
print(Eul2Axa(Theta))

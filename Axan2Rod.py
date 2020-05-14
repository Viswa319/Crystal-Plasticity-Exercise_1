from modulus import normalize
import math
import numpy as np
#This function transforms from Axis angle pair to Rodrigues vector representation
def Axa2Rod(N):
    rho = np.zeros((len(N),len(N[0]))) #Creating array with zeros in it
    for i in range(0,len(N)):
        if N[i][0:4] == [0,0,1,0]: #This is for a special case i.e. if rotation angle is zero
            rho[i][0:4] = [0,0,-1,0] 
        else:
            rho[i][0:3] = normalize(N[i][0:3]) #Normalizing the vector part of axis angle pair and assigning it to Rodrigues vector part
            W = math.radians(N[i][3]) #Converting angle from degrees to radians
            rho[i][3] = np.round(math.tan(W/2)) #Assigning length of the Rodrigues vector as fourth parameter to the Rodrigues vector
    return rho
# Testing the function for few values
N = [[0,0,1,0],[0,0,1,90],[0,0,1,180]]
print(Axa2Rod(N))

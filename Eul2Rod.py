from Eul2Axan import Eul2Axa
from Axan2Rod import Axa2Rod
#This function transforms Euler angles  to Miller indices
def Eul2Rod(Theta):
    for i in range(0,len(Theta)):
        N = Eul2Axa(Theta) #Transforming Euler angles to axis angle pair and then transforming
        rho = Axa2Rod(N) # axis angle pair to Rodrigues representation
    return rho 
# Testing the function for few values
Theta = [[0,0,0],[90,0,0],[180,0,0]]
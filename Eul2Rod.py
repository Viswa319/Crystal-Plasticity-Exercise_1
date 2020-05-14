from Eul2Axan import Eul2Axa
from Axan2Rod import Axa2Rod
#This function transforms Euler angles  to Miller indices
def Eul2Rod(Theta):
    N = Eul2Axa(Theta) #Transforming Euler angles to axis angle pair and then transforming
    rho = Axa2Rod(N) # axis angle pair to Rodrigues representation
    return rho 
# Testing the function for few values
Theta = [[0,0,0],[90,0,0],[180,0,0]]
#This function takes input of vector of Euler indices of size (n,3) where n is the number of sets of euler angles
print(Eul2Rod(Theta))
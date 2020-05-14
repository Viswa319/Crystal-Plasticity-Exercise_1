from Eul2Axan import Eul2Axa
from Axan2Rod import Axa2Rod
def Eul2Rod(Theta):
    for i in range(0,len(Theta)):
        N = Eul2Axa(Theta)
        rho = Axa2Rod(N)
    return rho 
# Testing the function for few values
Theta = [[0,0,0],[90,0,0],[180,0,0]]
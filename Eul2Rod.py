from Eul2Axan import Eul2Axa
from Axan2Rod import Axa2Rod
def Eul2Rod(x,y,z):
    N = Eul2Axa(x,y,z)
    return(Axa2Rod(N))
Eul2Rod(360,0,360)
from Eul2Axan import Eul2Axa
from Axan2Rod import Axa2Rod
def Eul2Rod(x,y,z):
    n = Eul2Axa(x,y,z)[0]
    w = Eul2Axa(x,y,z)[1]
    return(Axa2Rod(n,w))
Eul2Rod(360,0,360)
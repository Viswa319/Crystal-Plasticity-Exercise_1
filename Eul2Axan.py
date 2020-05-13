import numpy as np
import math
def Eul2Axa(x,y,z):
    X = math.radians(x)
    Y = math.radians(y)
    Z = math.radians(z)
    t = math.tan(Y/2)
    sigma = (0.5)*(X+Z)
    delta = (0.5)*(X-Z)
    tau = math.sqrt((t**2)+(math.sin(sigma))**2)
    alpha = 2*(math.atan2(tau,math.cos(sigma)))
    P = -1
    n = np.zeros(3)
    if round(alpha,6) == 0:
        n[0] = 0
        n[1] = 0
        n[2] = 1
        w = 0 
    elif alpha < math.pi:
        n[0] = np.round(-P*t*((tau)**(-1))*(math.cos(delta)),6)
        n[1] = np.round(-P*t*((tau)**(-1))*(math.sin(delta)),6)
        n[2] = np.round(-P*((tau)**(-1))*(math.sin(sigma)),6)
        w = np.round(math.degrees(alpha),6)
    elif alpha > math.pi :
        n[0] = np.round(P*t*((tau)**(-1))*(math.cos(delta)),6)
        n[1] = np.round(P*t*((tau)**(-1))*(math.sin(delta)),6)
        n[2] = np.round(P*((tau)**(-1))*(math.sin(sigma)),6)
        w =  np.round(math.degrees((2*math.pi)-alpha),6)
    return(n,w)
print(Eul2Axa(0,0,0))

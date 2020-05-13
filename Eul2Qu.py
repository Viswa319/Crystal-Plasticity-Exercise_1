import math
import numpy as np
def Eul2Qu(x,y,z):
    X = math.radians(x)
    Y = math.radians(y)
    Z = math.radians(z)
    sigma = 0.5*(X+Z)
    delta = 0.5*(X-Z)
    c = math.cos(Y*0.5)
    s = math.sin(Y*0.5)
    P = -1
    q = np.zeros(4)
    q[0] = c*math.cos(sigma)
    q[1] = -P*s*math.cos(delta)
    q[2] = -P*s*math.sin(delta)
    q[3] = -P*c*math.sin(sigma)
    return q
print(Eul2Qu(90,0,0))
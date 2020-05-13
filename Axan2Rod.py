from modulus import normalize
import math
import numpy as np
def Axa2Rod(n,w):
    Rho = normalize(n)
    W = math.radians(w)
    rh = np.round(math.tan(W/2))
    return Rho,rh
n = [0,0,1] 
w = 180
print(Axa2Rod(n,w))

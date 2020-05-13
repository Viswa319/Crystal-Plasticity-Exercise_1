import math
import numpy as np
from modulus import modulus, normalize
def Rod2Axan(rho,Rho):
    n = normalize(rho)
    W = 2*(math.atan(Rho))
    w = round(math.degrees(W),5)
    return n,w
rho = [0, 0, 1]
Rho = math.inf
A = Rod2Axan(rho,Rho)
print(A[0])


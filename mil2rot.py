# Crystal-Plasticity-Exercises
import numpy as np
from cross_product import cross_product
from modulus import modulus
from modulus import normalize
#Function transforms Miller indices to rotation matrix
def mil2rot(Dir,Pla):#Input direction miller indices and planar miller indices respectively
    b = normalize(Dir)
    n = normalize(Pla)
    t = cross_product(n,b)/(modulus(cross_product(n,b)))
    A = np.zeros((3,3))
    for i in range(0,len(b)):
            A[i,0] = b[i]
            A[i,1] = t[i]
            A[i,2] = n[i]
    return A
Dir = [1,0,0]
Pla = [0,1 ,0]
print(mil2rot(Dir,Pla))
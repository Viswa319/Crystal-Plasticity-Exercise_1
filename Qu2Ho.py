import math
import numpy as np
from modulus import modulus
#This function transforms quarternions to homochoric representation
def Qu2Ho(q):
    h = np.zeros((len(q),3))
    w = np.zeros(len(q))
    s = np.zeros(len(q))
    f = np.zeros(len(q))
    n = np.zeros((len(q),3))
    for j in range(0,len(q)):
        w[j] = 2*math.acos(q[j][0]) #first converting scalar part of quarternion to angle of rotation  
        if w[j] != 0: #If angle of rotation is not equal to zero the following program works
            s[j] = 1/modulus((q[j][1:4])) 
            f[j] = 3*(w[j] - math.sin(w[j]))/4
            for i in range(0,len(n)):
                n[j][i] = s[j]*(q[j][i+1]) #converting vector part of quarternions to axis vector and then transforming 
                h[j][i]  = n[j][i]*(f[j]**(1/3))#homochoric representation
    return h
# Testing the function for few values
#Input array of quarternions of size (n,4) where n will be the number of set of quarternions
q = [[1.0000000, 0.0000000, 0.0000000, 0.0000000],[0.7071068 ,0.0000000, 0.0000000, 0.7071068],[0.0000000 ,0.0000000, 0.0000000, 1.0000000]]
print(Qu2Ho(q))
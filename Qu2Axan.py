import math
import numpy as np
from permutation_tensor import sgn
from modulus import modulus
#This function transforms quarternions to axis angle pair representation
def Qu2Axan(q):
    n = np.zeros((len(q),4)) #Creating array with zeros in it
    for L in range(0,len(q)):
        n[L][3] = round(math.degrees(round(2*math.acos(q[L][0]),5)))#Calculating angle 
        if n[L][3] == 0: #special case if angle of rotation is 0
            n[L] = [0,0,1,0]
        else:
            if q[L][0] == 0: #if scalar part of quarternion is 0
                n[L][0:3] = [q[L][1],q[L][2],q[L][3]] #calculating axis 
                n[L][3] = math.degrees(math.pi) #equating angle to pi
            else:
                s = sgn(q[L][0])/(modulus(q[L][1:4]))
                for i in range(0,3):
                    n[L][i] = s*q[L][i+1]
    return n
# Testing the function for few values
q = [[1.0000000, 0.0000000, 0.0000000, 0.0000000],[0.7071068 ,0.0000000, 0.0000000, 0.7071068],[0.0000000 ,0.0000000, 0.0000000, 1.0000000]]
print(Qu2Axan(q))
import math
import numpy as np
from modulus import modulus
def Ho2Axan(h):
    gamma = np.zeros(16)
    for i in range(0,4):
        if i == 0:
            gamma[(4*i)+1] = 1.000000000001885
            gamma[(4*i)+2] = -0.500000000219485
            gamma[(4*i)+3] = -0.024999992127593
            gamma[(4*i)+4] = -0.003928701544781
        if i == 1:
            gamma[(4*i)+1] = -0.000815270153545
            gamma[(4*i)+2] = -0.000200950042612
            gamma[(4*i)+3] = -0.000023979867761
            gamma[(4*i)+4] = -0.000082028689266
        if i == 2:
            gamma[(4*i)+1] = 0.000124487150421
            gamma[(4*i)+2] = -0.000174911421482
            gamma[(4*i)+3] = 0.000170348193414
            gamma[(4*i)+4] = -0.000120620650041
        if i == 3:
            gamma[(4*i)+1] = 0.000059719705869
            gamma[(4*i)+2] = -0.000019807567240
            gamma[(4*i)+3] = 0.000003953714684
            gamma[(4*i)+4] = -0.000000365550014
        H = (modulus(h))**2
        if H == 0:
            n = [0,0,1]
            w = 0
            return n,w
        else:
            h1 = np.zeros(len(h))
            for i in range(0,len(h)):
                h1[i] = (h[i])/math.sqrt(H)
            s = 0
            for i in range(1,len(gamma)+1):
                s = s + (gamma[i-1])*(H**[i-1])
            n = h1
            w = math.degrees(2*math.acos(s))
            return n,w
h = [0.0000000, -0.0000000, -0.7536693]
print(Ho2Axan(h))
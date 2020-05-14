import math
import numpy as np
from modulus import modulus
#This function transforms homochoric representation to axis angle pair representation
def Ho2Axan(h):#Input homochoric vector of size(n,3) where n is the number of sets of homochoric vectors
    n = np.zeros((len(h),4)) #Creating array with zeros in it
    H = np.zeros(len(h))
    for J in range(0,len(h)):
        gamma = np.zeros(16) #Creating zero vector of size 16
        for i in range(0,4): #Assigning gamma vector which is given in the Rowenhorst paper
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
            H[J] = (modulus(h[J]))**2
            if H[J] == 0: #special case for H = 0 
                n[J] = [0,0,1,0]
                return n
            else:
                for j in range(0,len(h[0])):
                    n[J][j] = (h[J][j])/math.sqrt(H[J])
                s = 0
                for k in range(1,len(gamma)+1):
                    s = s + (gamma[k-1])*((H[J])**(k-1))
                n[J][3] = math.degrees(2*math.acos(s))
                return n
h = [[0.0000000 ,0.0000000 ,0.0000000],[0.0000000, 0.0000000, 0.7536693]]
print(Ho2Axan(h))
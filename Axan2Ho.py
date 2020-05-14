import math
import numpy as np
#This function transforms from Axis angle pair to Homochoric representation
def Axan2Ho(N):
    h = np.zeros((len(N),len(N[0])-1)) #Creating array with zeros in it
    for j in range(0,len(N)):
        W = math.radians(N[j][3])  #This converts angle from degrees to radians
        f = ((0.75)*(W-math.sin(W)))**(1/3) #Initializing a function f  
        for i in range(0,len(h)):
            h[j][i] = f*N[j][i] #Applying transformation from axis-angle pair to homochoric representation  
    return h
# Testing the function for few values
N = [[0,0,1,0],[0,0,1,90],[0,0,1,180]]
print(Axan2Ho(N))
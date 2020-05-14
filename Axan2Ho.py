import math
import numpy as np
def Axan2Ho(N):
    h = np.zeros((len(N),len(N[0])-1))
    for j in range(0,len(N)):
        W = math.radians(N[j][3])
        f = ((0.75)*(W-math.sin(W)))**(1/3)
        for i in range(0,len(h)):
            h[j][i] = f*N[j][i]
    return h
N = [[0,0,1,0],[0,0,1,90],[0,0,1,180]]
print(Axan2Ho(N))
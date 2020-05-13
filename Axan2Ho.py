import math
import numpy as np
def Axan2Ho(n,w):
    W = math.radians(w)
    f = ((0.75)*(W-math.sin(W)))**(1/3)
    h = np.zeros(len(n))
    for i in range(0,len(h)):
        h[i] = f*n[i]
    return h
n = [0,-0,-1]
w = 90
print(Axan2Ho(n,w))
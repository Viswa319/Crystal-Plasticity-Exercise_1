from Eul2Rot import Eul2Rot
from SymmopCub432 import SymmopCub432
from modulus import normalize
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
def circle(r):
    x=np.linspace(-r,r,1000)
    y=np.sqrt(r*r - x*x)
    return x,y
def Stereographic_projection(Eulerangles,Unitnormal):
    Rotation_matrix = Eul2Rot(Eulerangles)
    Sym = SymmopCub432()
    Unitnormal = normalize(Unitnormal)
    Global_coordinates = np.transpose(Unitnormal).dot(Rotation_matrix)
    Stereographic_coordinates = []
    for i in range(0,len(Sym)):
        temp = Global_coordinates.dot(Sym[i])
        x = temp[0][0]
        y = temp[0][1]
        z = temp[0][2]
        if z > -1:
            val = [(x)/(1+z),(y),(1+z)]
            Stereographic_coordinates.append(val)
        else:
            val = [(x)/(1-z),(y),(1-z)]
            Stereographic_coordinates.append(val)
    Stereo = np.array(Stereographic_coordinates)
    x,y = circle(Stereo[:,0].max())
    fig,ax = plt.subplots(ncols=2,figsize=(12,6))
    ax[0].scatter(Stereo[:,0],Stereo[:,1])
    ax[0].plot(x,y,color='blue')
    ax[0].plot(x,-y,color='blue')
    theta = np.zeros(len(Stereo[:,0]))
    r = np.zeros(len(Stereo[:,0]))
    for i in range(0,len(Stereo[:,0])):
        r[i] = np.sqrt((Stereo[:,0][i]**2)+(Stereo[:,1][i]**2))
        theta[i] = math.atan(Stereo[:,0][i]/Stereo[:,1][i])
    ax[1].scatter(r,theta)
    plt.show()
Unitnorm = [0,1,1]
Eulerangle = [[0,45,0]]
Stereographic_projection(Eulerangle,Unitnorm)
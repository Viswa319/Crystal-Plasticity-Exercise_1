from Eul2Rot import Eul2Rot
from SymmopCub432 import SymmopCub432
from modulus import normalize
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from MatVecmult import MatVecmult
def circle(r):
    x=np.linspace(-r,r,1000)
    y=np.sqrt(r*r - x*x)
    return x,y
def Stereographic_projection(Eulerangles,Unitnormal):
    Rotation_matrix = Eul2Rot(Eulerangles)
    Sym = SymmopCub432()
    Global_coordinates = np.zeros((len(Eulerangles),3))
    Stereographic_coordinates = np.zeros((len(Eulerangles),24,2))
    fig,ax = plt.subplots(ncols=2,figsize=(12,6))
    for S in range(0,len(Eulerangles)):
        Unitnormal = normalize(Unitnormal)
        Global_coordinates[S] = MatVecmult(Rotation_matrix[S],Unitnormal)
        temp = np.zeros((len(Sym),2))
        X = np.zeros(len(Sym))
        Y = np.zeros(len(Sym))
        Z = np.zeros(len(Sym))
        for i in range(0,len(Sym)):
            MatVecmult(Sym[i],Global_coordinates[S])
            X[i] = MatVecmult(Sym[i],Global_coordinates[S])[0]
            Y[i] = MatVecmult(Sym[i],Global_coordinates[S])[1]
            Z[i] = MatVecmult(Sym[i],Global_coordinates[S])[2]
            if Z[i] > -1:
                Stereographic_coordinates[S][i][0] = (X[i])/(1+Z[i])
                Stereographic_coordinates[S][i][1] = (Y[i])/(1+Z[i])
            else:
                Stereographic_coordinates[S][i][0] = (X[i])/(1-Z[i])
                Stereographic_coordinates[S][i][1] = (Y[i])/(1-Z[i])
        #x,y = circle(max(Stereographic_coordinates[S][:,0]))
        ax[0].scatter(Stereographic_coordinates[S][:,0],Stereographic_coordinates[S][:,1],color='blue')
        #ax[0].plot(x,y,color='blue')
        #ax[0].plot(x,-y,color='blue')
        theta = np.zeros(len(Stereographic_coordinates[S][:,0]))
        r = np.zeros(len(Stereographic_coordinates[S][:,0]))
        for i in range(0,len(Stereographic_coordinates[S][:,0])):
            r[i] = np.sqrt((Stereographic_coordinates[S][:,0][i]**2)+(Stereographic_coordinates[S][:,1][i]**2))
            theta[i] = math.atan(Stereographic_coordinates[S][:,0][i]/Stereographic_coordinates[S][:,1][i])
        ax[1].scatter(r,theta,color='blue')
    plt.show()
    #return(Stereographic_coordinates)
Unitnorm = [0,1,1]
Eulerangle = [[60,50,80],[9,10,75],[10,8,60]]
Stereographic_projection(Eulerangle,Unitnorm)
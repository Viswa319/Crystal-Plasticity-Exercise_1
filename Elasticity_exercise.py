# Sai Viswanadha Sastry Upadhyayula
# 65130
# Crystal Plasticity
# This program gives elastic material constants taking stiffness matrix as input
import numpy as np
import math
from modulus import modulus
def StiffnessMatrix():
    # This function generates 
    C = np.zeros((6,6))
    ClassOfMaterials = ['Triclinic','Monoclinic','Orthotropic','Transversely Isotropic','Cubic','Isotropic']
    print(ClassOfMaterials)
    CrystalType = input('Please specify crystal type from the above list:')
    if CrystalType == ClassOfMaterials[0]:
        C[0][0] = float(input('Input the value of C_11:'))
        C[1][1] = float(input('Input the value of C_22:'))
        C[2][2] = float(input('Input the value of C_33:'))
        C[3][3] = float(input('Input the value of C_44:'))
        C[4][4] = float(input('Input the value of C_55:'))
        C[5][5] = float(input('Input the value of C_66:'))
        C[0][1] = C[1][0] = float(input('Input the value of C_12:'))
        C[0][2] = C[2][0] = float(input('Input the value of C_13:'))
        C[0][3] = C[3][0] = float(input('Input the value of C_14:'))
        C[0][4] = C[4][0] = float(input('Input the value of C_15:'))
        C[0][5] = C[5][0] = float(input('Input the value of C_16:'))
        C[1][2] = C[2][1] = float(input('Input the value of C_23:'))
        C[1][3] = C[3][1] = float(input('Input the value of C_24:'))
        C[1][4] = C[4][1] = float(input('Input the value of C_25:'))
        C[1][5] = C[5][1] = float(input('Input the value of C_26:'))
        C[2][3] = C[3][2] = float(input('Input the value of C_34:'))
        C[2][4] = C[4][2] = float(input('Input the value of C_35:'))
        C[2][5] = C[5][2] = float(input('Input the value of C_36:'))
        C[3][4] = C[4][3] = float(input('Input the value of C_45:'))
        C[3][5] = C[5][3] = float(input('Input the value of C_46:'))
        C[4][5] = C[5][4] = float(input('Input the value of C_56:'))
    elif CrystalType == ClassOfMaterials[1]:
        C[0][0] = float(input('Input the value of C_11:'))
        C[1][1] = float(input('Input the value of C_22:'))
        C[2][2] = float(input('Input the value of C_33:'))
        C[3][3] = float(input('Input the value of C_44:'))
        C[4][4] = float(input('Input the value of C_55:'))
        C[5][5] = float(input('Input the value of C_66:'))
        C[0][1] = C[1][0] = float(input('Input the value of C_12:'))
        C[0][2] = C[2][0] = float(input('Input the value of C_13:'))
        C[0][5] = C[5][0] = float(input('Input the value of C_16:'))
        C[1][2] = C[2][1] = float(input('Input the value of C_23:'))
        C[1][5] = C[5][1] = float(input('Input the value of C_26:'))
        C[2][5] = C[5][2] = float(input('Input the value of C_36:'))
        C[3][4] = C[4][3] = float(input('Input the value of C_45:'))
    elif CrystalType == ClassOfMaterials[2]:
        C[0][0] = float(input('Input the value of C_11:'))
        C[1][1] = float(input('Input the value of C_22:'))
        C[2][2] = float(input('Input the value of C_33:'))
        C[3][3] = float(input('Input the value of C_44:'))
        C[4][4] = float(input('Input the value of C_55:'))
        C[5][5] = float(input('Input the value of C_66:'))
        C[0][1] = C[1][0] = float(input('Input the value of C_12:'))
        C[0][2] = C[2][0] = float(input('Input the value of C_13:'))
        C[1][2] = C[2][1] = float(input('Input the value of C_23:'))
    elif CrystalType == ClassOfMaterials[3]:
        C[0][0] = C[1][1] = float(input('Input the value of C_11:'))
        C[2][2] = float(input('Input the value of C_33:'))
        C[3][3] = C[4][4] = float(input('Input the value of C_44:'))
        C[0][1] = C[1][0] = float(input('Input the value of C_12:'))
        C[0][2] = C[2][0] = C[1][2]= C[2][1]= float(input('Input the value of C_13:'))
        C[5][5] = (1/2)*(C[0][0]-C[0][1])
    elif CrystalType == ClassOfMaterials[4]:
        C[0][0] = C[1][1] = C[2][2]= float(input('Input the value of C_11:'))
        C[3][3] = C[4][4] = C[5][5] = float(input('Input the value of C_66:'))
        C[0][1]=C[1][0]=C[0][2] = C[2][0] = C[1][2]= C[2][1]= float(input('Input the value of C_12:'))
    elif CrystalType == ClassOfMaterials[5]:
        Lambda = float(input('Input the value of Lame constant lambda:'))
        mu = float(input('Input the value of Lame constant mu:'))
        C[0][0] = C[1][1] = C[2][2]= Lambda+(2*mu)
        C[3][3] = C[4][4] = C[5][5] = mu
        C[0][1]=C[1][0]=C[0][2] = C[2][0] = C[1][2]= C[2][1]= Lambda
    else: 
        print('Your specified crystal system is not in the list, please check the spelling and give input again')
    return C
C = StiffnessMatrix()
S = np.linalg.inv(C) #Compliance Matrix
A = (2*(S[0][0]-S[0][1]))/(S[3][3]) #Anisotropy factor
def CosineAngle(x,y):
    CosTheta = ((x[0]*y[0])+(x[1]*y[1])+(x[2]*y[2]))/(modulus(x)*modulus(y))
    return CosTheta
def YoungsModulus(dir,StiffnessMatrix):
    S = np.linalg.inv(C)
    alpha = CosineAngle(dir,[1,0,0])
    beta = CosineAngle(dir,[0,1,0])
    gamma = CosineAngle(dir,[0,0,1])
    E = S[0][0] - ((2*(S[0][0]-S[0][1])-S[3][3])*(((alpha**2)*(beta**2))+((alpha**2)*(gamma**2))+((gamma**2)*(beta**2))))
    YoungsModulus = 1/E
    print(alpha,beta,gamma)
    print(S)
    return YoungsModulus
dir = [1,1,0]
print(YoungsModulus(dir,C))
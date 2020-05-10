import math
def Rot2Eul(A):
    if A[2][2] == 1:
        Y = 0
        X = math.atan2(A[0][1],A[0][0])
        Z = X
    else:
        Y = math.acos(A[2][2])
        X = math.atan2((A[2][0]/math.sin(Y)),-(A[2][1]/math.sin(Y)))
        Z = math.atan2((A[0][2]/math.sin(Y)),(A[1][2]/math.sin(Y)))
    x = math.degrees(X)
    y = math.degrees(Y)
    z = math.degrees(Z)
    return x,y,z
A = [[ 1, 0, 0],
 [0 , 0,  1],
 [ 0 , -1 , 0]]
print(Rot2Eul(A))

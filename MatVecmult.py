import numpy as np
def MatVecmult(matrix,vector):
    if len(matrix) == len(vector):
        output = np.zeros(len(vector))
        for i in range(0,len(vector)):
            for j in range(0,len(matrix)):
                output[i] = output[i]+vector[j]*matrix[j][i]
        return output
    else:
        print("Vector length and matrix length must be same")

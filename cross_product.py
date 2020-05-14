import numpy as np
from permutation_tensor import permutation
#This function returns a cross product of two vectors
def cross_product(a,b):
    n = np.zeros(len(a))
    for k in range(0,len(n)):
        for i in range(0,len(a)):
            for j in range(0,len(b)):
                n[k] = n[k]+(permutation(i,j,k)*a[i]*b[j]) #Calculating cross product of two vectors and assigning it to a vector 
    return n
a = [1,2,3]
b = [6,8,9]
print(cross_product(a,b))
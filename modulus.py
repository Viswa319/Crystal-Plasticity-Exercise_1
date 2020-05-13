import numpy as np
def modulus(a):
    sum1 = 0
    for i in range(0,len(a)):
        sum1 = sum1 + (a[i])**2
    mod = np.sqrt(sum1)
    return mod
def normalize(a):
    b = np.zeros(len(a))
    for i in range(0,len(a)):
        b[i] = a[i]/(modulus(a))
    return b
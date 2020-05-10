from permutation_tensor import permutation
def cross_product(a,b):
    m = []
    n = [0]*len(a)
    for k in range(0,len(n)):
        for i in range(0,len(a)):
            for j in range(0,len(b)):
                n[k] = n[k]+(permutation(i,j,k)*a[i]*b[j])
        m.append(n[k])
    return m
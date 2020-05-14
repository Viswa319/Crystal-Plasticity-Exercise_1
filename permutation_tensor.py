#This function basically gives values for permutation tensor
# i.e. value for even permutations is 1, value for odd permutations is -1 and if two or more numbers repeat value is 0
def permutation(i,j,k):
    if i == j or j == k or i==k:
        return 0
    elif i ==0 and j == 1 and k == 2:
        return 1
    elif i ==1 and j == 2 and k == 0:
        return 1
    elif i ==2 and j == 0 and k == 1:
        return 1
    elif i ==0 and j == 2 and k == 1:
        return -1
    elif i ==1 and j == 0 and k == 2:
        return -1
    elif i ==2 and j == 1 and k == 0:
        return -1           
#function which returns 1 if x is positive and -1 if x is negative
def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1   
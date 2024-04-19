def swap(X,i,j):
    pivot = X[i]
    X[i] = X[j]
    X[j] = pivot
    return X

def mex(X):
    res = 0
    ultimo_que_no_esta = 0
    #O(n)
    for i in range(len(X)):
        if(X[i]<len(X)):
            swap(X,i,X[i]) 
    #O(n)
    for e in X:
        if e == ultimo_que_no_esta:
            ultimo_que_no_esta += 1
            res += ultimo_que_no_esta
        else:
            res += ultimo_que_no_esta
    return res


print(mex([0,1,3]))
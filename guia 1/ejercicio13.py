#Idea:
# Como los multicjtos (llamemoslos X Y)  estan ordenados puedo chequear
# x[i] con y[j] (incialmente i,j=0) si la diferencia es menor o igual a 1.
# Caso contrario verifico si x[0] es mayor a y[0] avanzo el j
# Caso x[0] es menor a y[0] avanzo el i
def ParejasdeBaile(X,Y):
    i = 0
    j = 0
    res = 0

    while i < len(X) and j < len(Y):
        if abs(X[i] - Y[j]) <= 1:
            res += 1
            i += 1
            j += 1
        else:
            if X[i] > Y[j]:
                j += 1
            else:
                i += 1

    return res
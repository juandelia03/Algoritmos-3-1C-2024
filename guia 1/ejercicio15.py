#mi estrategia va a ser ordenar la lista (O(nlogn)) y depsues sumar de izquierda a derecha.
#Los numeros más grandes los quiero sumar últimos asi los sumo menos veces, si los sumase 
#al prcipio ya serían parte de la suma parcial que se seguría sumando con todo el resto.
def suma_golosa(X):
    costo = 0
    #O(nlogn)
    X.sort()
    #O(n)
    for i in range(len(X)-1):
        #agrego al costo la suma del actual mas el siguiente
        costo += X[i] + X[i+1]
        #actualizo el siguiente a la suma con su anterior
        X[i+1] = X[i] + X[i+1]
    suma = X[-1]
    return costo,suma

print(suma_golosa([5,2,1]))        



#Si elc cjto lo recibimos como una lista desordenada podemos conseguir la
# sublista que maximiza la suma de tamaño k ordenando la lista (O(nlogn))
# y devolviendo la sub lista de largo k que llegue hasta el final de la lista
def sumaSelectiva(X,k):
    n = len(X)
    X.sort()
    s = X[n-k:n]
    return s,sum(s)

print(sumaSelectiva([1,2,1,4,1],2))
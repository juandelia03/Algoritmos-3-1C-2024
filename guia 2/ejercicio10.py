#Idea:
# primero parto al medio ambas listas
# si la diferencia del indice a la izquierda es mayor  a la diferencia del medio
# a medida que siga mirando a la izquierda la diferencia solo se puede agrandar (xq el nro de a se hace mas chico y el de b se hace mas grande)
# entonces me quedo solo con la parte derecha del arreglo
# Lo mismo pasa en el caso de mirar el indice derecho.

def diferencia(x,y):
    return abs(x-y)

def dif_min(a,b):
    m = len(a) // 2
    if(len(a)==3):
        return min(min(diferencia(a[0],b[0]),diferencia(a[1],b[1])),(diferencia(a[2],b[2])))
    
    if(len(a)==2):
        return min(diferencia(a[0],b[0]),diferencia(a[1],b[1]))
    #el medio tiene menos diferencia que el lado izquierdo
    if(diferencia(a[m],b[m]) < diferencia(a[m-1],b[m-1])):
        return dif_min(a[m:len(a)],b[m:len(a)])
    #el medio tiene menos diferencia q el lado derecho
    elif(diferencia(a[m],b[m]) < diferencia(a[m+1],b[m+1])):
        return dif_min(a[0:m+1],b[0:m+1])
    

A = [1, 2, 3, 4]
B = [6, 4, 2, 1]

print(dif_min(A,B))


# complejidad:
# c.b es O(1)
# c.r:
# T(n) = 1.T(n/2) + O(1)
# por teorema maestro (a=1,b=2,c=0):
# log en base b  de a = 0 == c -> T(n) = O(n^0.logn) = O(log n)  
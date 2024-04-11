class Nodo:
    def __init__(self, data):
        self.data = data
        self.izq = None
        self.der = None

#Altura es O(n). no se si esta bien definida, creo que si.
def altura(n):
    if n == None:
        return 0
    else:
        Hi = altura(n.izq)
        Hd = altura(n.der)
        return max(Hi, Hd) + 1

#No se me ocurre ningun caso en el que la distancia maxima no sea
#La suma del subarbol izq + subarbol der. Posiblemente me equivoque.
def DistanciaMaxima(n):
    return altura(n.izq) + altura(n.der)


nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)

nodo1.izq = nodo2
nodo1.der = nodo3
nodo2.izq = nodo4
nodo2.der = nodo5
nodo4.izq = nodo6
#              1
#           2    3
#         4  5  
#       6
print("Distancia Máxima:", DistanciaMaxima(nodo1)) 

#Complejidad : C.B : Ø(1) C.R: T(n) = 2T(n/2) + cte
#Por teorema maestro a=2 b=2 c=0 -> log base b de a = 1 > c =0 -> Ø(n)
# Que se podia intuir porque solamente haciamos altura de los dos sub arboles que es recorrer n eltos
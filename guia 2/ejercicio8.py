#voy a asumir que n>4 siempre es potencia de dos para que quede mas simple
#asi cada vez q parto matrices voy a llegar al caso base de una de 4x4
#si no tendria que ver el caso base de que cuando son de tamaño menor mirar
#cada elemento uno a uno y chequear si es false

#Lease como pseudocodigo:

#Asumimos que es O(1)
def conjuncionSubmatriz(M,i0,i1,j0,j1):
    #devuelve true si no hay ningun false en la sub m
    #false c.c
    return False

#Ø(4) = Ø(1)
def BuscarPosicion(M,i0,i1,j0,j1):
    #dada una submatriz de 4x4 y su posicion respecto a la matriz original
    #busca la posicion en la matriz de algun false
    return (i0,j1)


#siempre que entre a esta funcion se que va a haber un falso en algun lado de la matriz
# 
def CazadorDeFalsos(m,i0,i1,j0,j1):
    #caso base 
    #Para el inciso B tendria que sumar uno a un contador
    #x cada falso que haya aca y al final de todo retornar el contador
    if len(m) == 4:
        return BuscarPosicion(m,i0,i1,j0,j1)
    
    #voy a partir la matriz en cuatro y con conjuncionSubmatriz
    #buscar en O(1) en que fraccion hay un falso y llamar a la rec solo con ese
    #Para el inciso B tendria que llamar a la recursion con todos en los que haya un falso
    #asi sumo cada vez que encuentro un Falso
    else:
        A = (m,i0,i1/2,j0,j1/2)
        B = (m,i0/2,i1,j0,j1/2)
        C = (m,i0,i1/2,j0/2,j1)
        D = (m,i0/2,i1,j0/2,j1)
        
        #asumo que conjuncion submatriz descarta todos los casos con indices inaccesibles 
        #Hay algun Falso en la particion superior izquierda
        if conjuncionSubmatriz(A) == False: return CazadorDeFalsos(A)
        if conjuncionSubmatriz(B) == False: return CazadorDeFalsos(B)
        if conjuncionSubmatriz(C) == False :return CazadorDeFalsos(C)
        if conjuncionSubmatriz(D) == False :return CazadorDeFalsos(D)

#Complejidad:
#a) En el inciso a solo agarro una submatriz xq me interesa recuperar una unica pos
#C.B: Ø(1) C.R: T(n) = 1.T(n/4) + cte -> a=1 b=4 c=0 log en base 4 de 1 = 0 == c
# Por teorema maestro T(n) = log n

#en el inciso B necesito tomar todas las mitades para sumar todos los falsos
# T(n) = 4.T(n/4) + cte -> a=4 b=4 c=0 log en base 4 de 4 = 1 > c =0
# entonces por teorema maestro:
# T(n) = Ø(n)


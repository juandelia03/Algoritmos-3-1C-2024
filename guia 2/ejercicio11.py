
#por consigna O(√j − i + 1) o O(raiz(n)) siendo n el largo de A[i:j+1]
def aparece(A, i, j, e):
    for k in range(i, j+1):
        if A[k] == e:
            return True
    return False


def ubicar(A,e,inicio,fin):
    m = (inicio+fin)//2
    if(inicio == fin):
        return inicio
    if(abs(inicio-fin)==1):
        if A[inicio] == e : return inicio
        else: return fin
    #si esta en la mitad izquierda(medio inclusive)
    if(aparece(A,inicio,m,e)):
        #aparece es O(raiz(n/2)) xq siempre calculo la mitad del arreglo
        return ubicar(A,e,inicio,m)
    #como podemos asumir que el elto esta 
    else:
        return ubicar(A,e,m+1,fin)
    
#C.B O(1)
# T(n) = T(n/2) + O(raiz(n))
#a=1 b=2 c=1/2 -> c> log en base b de a
#por teorema maestro T(n) = O(n^(1/2)) = O(raiz(n))
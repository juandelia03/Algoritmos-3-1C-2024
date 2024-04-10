#suponer f potencia(A,n) tq: A es matriz 4x4 n entero que es potencia de 2 y devuelve A^n
#Asumimos tmb que esta definido el producto para matrices
def Potencia(A,n):
    return 1


def PotenciaSum(A,n):
    if n == 1:
        return A
    else:
        M = PotenciaSum(A,n/2)
        return M + M*Potencia(A,n/2)
    
#explico:
# por ejemplo para una matriz A y n=8 (n siempre es potencia de 2)
# quiero A^1+ A^2 + A^3 + A^4 + A^5+ A^6 + A^7 + A^8
# puedo decir que A^5+ A^6 + A^7 + A^8 = B
# B a su vez es igual a (A^1+ A^2 + A^3 + A^4)*A^4
# que es a su vez f(A,8/2)*Potencia(A,8/2) o en gral f(A,n/2)*Potencia(A,n/2) 
# entonces para recuperar la expresion que quiero:
# f(A,n/2) + f(A,n/2)*Potencia(A,n/2)

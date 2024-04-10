def mas_a_la_izquierda(A):
    m = int(len(A)/2)
    l = A[:m]
    r = A[m:]
    suma_l = sum(l)
    suma_d = sum(r)
    if suma_l > suma_d:
        if (len(A) == 2):
            return True
        return (mas_a_la_izquierda(l) and mas_a_la_izquierda(r))
    else:
        return False


def PotenciaLog(a,b):
    # Ø(1)
    if b ==1:
        return a
    # Ø(1)
    if(b==2):
        return a*a
    if b % 2 == 0:
        #T(n) = 1.T(n/2) + Ø(1)
        subcaso = PotenciaLog(a,b/2)
        return subcaso * subcaso
    else:
        #T(n) = 1.T(n/2) + Ø(1)
        subcaso = PotenciaLog(a,b//2)
        return subcaso * subcaso * a


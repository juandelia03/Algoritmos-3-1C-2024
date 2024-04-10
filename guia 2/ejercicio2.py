def I_Espejo(A,i,f):
    if((i==f) and A[i] != i) or (f<i):
        return False
    m = (f+i)//2
    if A[m] == m : return True
    if A[m] >  m :return I_Espejo(A,i,m-1)
    if A[m] < m: return I_Espejo(A,m+1,f)


# lista = [-4, -2, -1, 0, 4, 6, 7]
# print(I_Espejo(lista,0,len(lista)-1))
#Como el Array esta desordenado se puede resolver con un heap
#sabemos que Array2Heap es O(n), una vez tengamos el heap
# es tan simple como tomar el primer elemento k veces
from heapq import _heapify_max, _heappop_max

def SumaSelectiva(X,k):
    res = []
    _heapify_max(X)
    for i in range(k):
        res.append(_heappop_max(X))
    return res , sum(res)

print(SumaSelectiva([1,2,1,4,1,1,1,11,2,3,5],2))
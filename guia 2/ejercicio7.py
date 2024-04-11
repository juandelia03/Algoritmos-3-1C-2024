# merge es Ø(n) n=len(arr1) + len(arr2)
counter = 0

def merge(arr1,arr2):
    global counter
    i=0
    j=0
    result=[]
    #mientras los dos tengan eltos
    while(i<len(arr1) and j<len(arr2)):
        if arr2[j]>arr1[i]:
            result.append(arr1[i])
            i+=1
        #caso desorden
        else:
            #i es cuantos ya meti del arr1
            #entonces len(arr1)-i me dice cuantos quedan del arr1 (del q deberia encontre elem desordenado)
            #que van a ser con la cantidad de pares desordenados que estoy sumando por ese elemento
            # counter += (len(arr1)-i)
            counter+=len(arr1)-i
            result.append(arr2[j])
            j+=1
    #si le quedan elementos a arr1 los mete
    while(i<len(arr1)):
        result.append(arr1[i])
        i+=1
    #si le quedan elementos a arr2 los mete
    while(j<len(arr2)):
        result.append(arr2[j])
        j+=1
    return result


def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left,right)

def DesordenSort(arr):
    mergeSort(arr)
    return counter


#La complejidad es C.B: Ø(1) C.R: T(n) = 2T(n/2) + n (el n por el merge)
#Por Teorema maestro -> a=2 b=2 c=1 log en base b de a = 1 = c -> T(n) = Ø(nlog n) 
print(DesordenSort([12, 11, 13, 5, 6, 7]))



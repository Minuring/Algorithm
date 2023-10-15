def qsort(array, low, high) :
    if low < high :
        p = partition(array, low, high)
        #print("Partition후 :   ",array)
        qsort(array, low, p-1)
        qsort(array, p+1, high)

def partition(v, low, high) :
    i, pivot = low, v[high]
    
    for j in range(low, high) :
        if v[j] > pivot : continue 
        
        v[j], v[i] = v[i], v[j]
        i += 1

    v[i],v[high] = v[high],v[i]
    return i
import random
for _ in range(1000) :
    input_list = [random.randint(1,100) for _ in range(0, 100)]
#print("정렬 전 : \t", input_list)
    qsort(input_list, 0, len(input_list)-1)
    print("정렬 후 : \t", input_list)

        
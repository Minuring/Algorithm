def partition(v, low, high) :
    i, pivot = low, v[high]

    for j in range(low, high) :
        if v[j] > pivot : continue
        
        v[j], v[i] = v[i], v[j]
        i += 1

    v[i],v[high] = v[high],v[i]
    return i


def selection(a, low, high, k):
    pivot = partition(a, low, high)
    if k < pivot:
        return selection(a, low, pivot-1, k)
    elif k == pivot:
        return a[k]
    else:
        return selection(a, pivot+1, high, k)


input_list = [40, 20, 50, 70, 65, 90, 35, 10, 15, 60, 55, 80, 25, 75]
K = input('(k-1) 값을 입력하라(0부터 ' + str((len(input_list)-1)) + '): ')
kth_smallest = selection(input_list, 0, len(input_list)-1, int(K))
print('{:2}번째 작은 수는 {:2}이다.'.format(int(K)+1, kth_smallest))

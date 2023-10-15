def qsort(array, low, high) :
    if low < high :
        p = partition(array, low, high)
        print("Partition후 :   ",array)
        qsort(array, low, p-1)
        qsort(array, p+1, high)

def partition(array, low, high) :
    pv, left, right = array[low], low+1, high

    while left < right :#엇갈리기 전까지

        while array[left] <= pv and left <= high:#피봇보다 큰거찾을떄까지
            left += 1

        while array[right] > pv and right >= low:#피봇보다 작은거찾을때까지
            right -= 1

        if left < right : #엇갈린거아니면 교환
            array[left], array[right] = array[right], array[left]

    #엇갈렸으니 피벗이랑 "RIGHT" 교환
    array[right], array[low] = array[low], array[right]
            

    return right

input_list = [50,85,2,3,4,1,51,25,32,62,6,143,32]
print("정렬 전 : \t", input_list)
qsort(input_list, 0, len(input_list)-1)
print("정렬 후 : \t", input_list)

        
import random
def merge_sort(array, low, high) :
    if low >= high :
        return
    
    mid = ( low + high ) // 2
    merge_sort(array, low, mid)
    merge_sort(array, mid+1, high)
    merge(array, low, mid, high)

def merge(array, low, mid, high) :
    sortedArray = []
    left, right = low, mid+1

    while left<=mid and right<=high :

        if array[left] <= array[right] :
            sortedArray.append(array[left])
            left += 1
        else :
            sortedArray.append(array[right])
            right += 1

    if left > mid : #왼쪽 리스트 먼저 끝
        for i in range(right, high+1) :
            sortedArray.append(array[i])
    else : #오른쪽 리스트 먼저 끝
        for i in range(left, mid+1) :
            sortedArray.append(array[i])

    array[low:high+1] = sortedArray
    
v=[random.randint(1,100) for _ in range(0, 10)]
merge_sort(v, 0, len(v)-1)
print(v)
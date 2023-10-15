def binarySearch_While (array, key) :
    low = 0
    high = len(array)-1

    while low <= high :
        mid = ( low + high ) // 2
        
        if key > array[mid] :
            low = mid + 1
        elif key < array[mid] :
            high = mid - 1
        else :
            return mid

    return -1

def binarySearch_Recursive (array, low, high, key) :
    if low > high : 
        return -1
    
    mid = ( low + high ) // 2

    if key > array[mid] :
        return binarySearch_Recursive(array, mid+1, high, key)
    elif key < array[mid] :
        return binarySearch_Recursive(array, low, mid-1, key)
    else :
        return mid

testArray = [3, 7, 8, 11, 23, 24, 31, 45]
print(binarySearch_While(testArray, 23))
print(binarySearch_Recursive(testArray, 0, len(testArray)-1, 7))


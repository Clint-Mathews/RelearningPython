def findMinMax(arr):
    min = max = arr[0]
    for i in range(1, len(arr)):
        min, max = arr[i] if min > arr[i] else min, arr[i] if max < arr[i] else max
    return min, max

def findMinMaxSort(arr):
    arr.sort() # Cant dop sort right now because im not sure what the best way is!
    return arr[0], arr[len(arr)-1]

def findMinDivideAndConquer(arr, left, right):
    if len(arr[left:right]) == 1:
        return arr[left:right][0]
    mid = int((left+right)/2)
    return min(findMinDivideAndConquer(arr, left, mid), findMinDivideAndConquer(arr, mid, right))

def findMaxDivideAndConquer(arr, left, right):
    if len(arr[left:right]) == 1:
        return arr[left:right][0]
    mid = int((left+right)/2)
    return max(findMaxDivideAndConquer(arr, left, mid), findMaxDivideAndConquer(arr, mid, right))


print(findMinMax([3,12,45,7,2,4,6]))
print(findMinMaxSort([3,12,45,7,2,4,6]))
print(findMinDivideAndConquer([3,12,45,7,2,4,6], 0, 6), findMaxDivideAndConquer([3,12,45,7,2,4,6], 0, 6))
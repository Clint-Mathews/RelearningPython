def binarySearch(arr, target):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = int(start + (end-start)/2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return -1

def binarySearchOrderAgnostic(arr, target):
    ascending = arr[0] < arr[1]
    start = 0
    end = len(arr)-1
    if ascending:
        while start <= end:
            mid = int(start + (end-start)/2)
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                start = mid+1
            else:
                end = mid-1
        return -1
    else:
        while start <= end:
            mid = int(start + (end-start)/2)
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                end = mid-1
            else:
                start = mid+1
        return -1


def binarySearchRecursive(arr,target,start,end):
    if start > end:
        return -1
    mid = int(start + (end-start)/2)
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binarySearchRecursive(arr, target, mid+1, end)
    else:
        return binarySearchRecursive(arr, target, start, mid-1)

data = [2, 4, 7, 9, 12, 15, 17, 38, 46, 89, 101]
index = binarySearch(data, 101)
if index != -1:
    print(index, data[index])
else:
    print("Target not found")

index = binarySearchRecursive(data, 101, 0, len(data))
if index != -1:
    print(index, data[index])
else:
    print("Target not found")




data = [2, 4, 7, 9, 12, 15, 17, 38, 46, 89, 101]
index = binarySearchOrderAgnostic(data, 101)
if index != -1:
    print(index, data[index])
else:
    print("Target not found")

data = [128,23,4,3,2,1]
index = binarySearchOrderAgnostic(data, 2)
if index != -1:
    print(index, data[index])
else:
    print("Target not found")

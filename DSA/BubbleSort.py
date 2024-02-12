def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[j] < arr[j-1]:
                swap(arr, j-1, j)

def bubbleSortOptimized(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)-i):
            if arr[j] < arr[j-1]:
                swap(arr, j-1, j)



def bubbleSortBetterOptimized(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(1,len(arr)-i):
            if arr[j] < arr[j-1]:
                swap(arr, j-1, j)
                swapped = True
        if not swapped:
            break

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

data = [6,3,4,2,1]
print("UnSorted", data)
bubbleSort(data)
print("Sorted", data)

data = [6,3,4,2,1]
print("UnSorted", data)
bubbleSortOptimized(data)
print("Sorted", data)

data = [6,1,1,1]
print("UnSorted", data)
bubbleSortBetterOptimized(data)
print("Sorted", data)
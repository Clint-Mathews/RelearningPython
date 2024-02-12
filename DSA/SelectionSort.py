def selectionSort(arr):
    for i in range(len(arr)):
        if i == len(arr)-1:
            return arr
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                swap(arr, i, j)


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

data = [6,3,4,2,1]
print("UnSorted", data)
selectionSort(data)
print("Sorted", data)
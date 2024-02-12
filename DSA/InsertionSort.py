def insertionSort(arr):
    for i in range(len(arr)-1):
        j = i+1
        while j > 0:
            if arr[j] < arr[j-1]:
                swap(arr, j, j-1)
                j -= 1
            else:
                break


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

data = [6,3,4,2,1]
print("UnSorted", data)
insertionSort(data)
print("Sorted", data)
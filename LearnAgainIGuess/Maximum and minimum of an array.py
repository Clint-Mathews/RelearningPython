# Input: arr[] = {3, 5, 4, 1, 9}
# Output: Minimum element is: 1
#               Maximum element is: 9
#
# Input: arr[] = {22, 14, 8, 17, 35, 3}
# Output:  Minimum element is: 3
#               Maximum element is: 35
import sys


def brute_force_find_min_max(arr: list) -> (int, int):
    minvalue = sys.maxsize
    maxvalue = - sys.maxsize

    for i in arr:
        if maxvalue < i:
            maxvalue = i
        elif minvalue > i:
            minvalue = i
    return minvalue, maxvalue


def brute_force_find_min_max_optimized(arr: list) -> (int, int):
    minvalue = maxvalue = 0

    if len(arr) == 1:
        return arr[0], arr[0]

    if arr[0] > arr[1]:
        minvalue = arr[1]
        maxvalue = arr[0]
    else:
        minvalue = arr[0]
        maxvalue = arr[1]

    for i in range(2, len(arr)):
        if maxvalue < arr[i]:
            maxvalue = arr[i]
        elif minvalue > arr[i]:
            minvalue = arr[i]
    return minvalue, maxvalue


def brute_force_sorting(arr: list) -> (int, int):
    arr.sort()
    return arr[0], arr[len(arr) - 1]


def divide_and_conquer(arr: list) -> (int, int):
    if len(arr) == 1:
        return arr[0], arr[0]
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[1], arr[0]
        else:
            return arr[0], arr[1]
    else:
        mid = int(len(arr) / 2)
        split_array1 = arr[0:mid]
        split_array2 = arr[mid:len(arr)]
        val1min, val1max = divide_and_conquer(split_array1)
        val2min, val2max = divide_and_conquer(split_array2)
        min_value = min(val1min, val2min)
        max_value = max(val1max, val2max)
        return min_value, max_value


if __name__ == '__main__':
    arr = [3, 5, 4, 1, 9]
    min_value, max_value = brute_force_find_min_max(arr)
    print('brute_force_find_min_max - min_value: ', min_value, ' max_value: ', max_value)
    min_value, max_value = brute_force_find_min_max_optimized(arr)
    print('brute_force_find_min_max_optimized - min_value: ', min_value, ' max_value: ', max_value)
    min_value, max_value = divide_and_conquer(arr)
    print('divide_and_conquer - min_value: ', min_value, ' max_value: ', max_value)
    min_value, max_value = brute_force_sorting(arr)
    print('brute_force_sorting - min_value: ', min_value, ' max_value: ', max_value)

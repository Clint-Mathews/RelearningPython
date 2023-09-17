import sys


def getMinMaxDivide(arr: list, low: int, high: int) -> (int, int):
    if low == high:
        return arr[low], arr[low]
    elif low + 1 == high:
        if arr[low] > arr[high]:
            return arr[high], arr[low]
        else:
            return arr[low], arr[high]
    else:
        mid = int((low + high) / 2)
        min_1, max_1 = getMinMaxDivide(arr, low, mid)
        min_2, max_2 = getMinMaxDivide(arr, mid, high)
        return min(min_1, min_2), max(max_1, max_2)


class Pair:
    def __init__(self):
        self.min = sys.maxsize
        self.max = -1 * sys.maxsize

    def getMinMaxSequential(self, arr: list):
        if len(arr) == 1:
            self.max = arr[0]
            self.min = arr[0]
        else:
            for i in arr:
                if i < self.min:
                    self.min = i
                if i > self.max:
                    self.max = i


if __name__ == "__main__":
    pair = Pair()

    arr = [22, 12, 1, 2, 1, 21]
    pair.getMinMaxSequential(arr)

    minVal, maxVal = getMinMaxDivide(arr, 0, len(arr) - 1)
    print(f'Sequential - max: {pair.max} ,min: {pair.min}')
    print(f'Divide & Conquer - max: {maxVal} ,min: {minVal}')

class MaxSumSubArray:
    def __init__(self, items):
        self.items = items

    def findMaxSumInSubArray(self) -> int:
        cur_sum = 0
        max_sum = self.items[0]
        start = 0
        end = 0
        pos = 0
        for index, item in enumerate(self.items):
            cur_sum += item
            if max_sum < cur_sum:
                start = pos
                end = index
                max_sum = cur_sum
            if cur_sum < 0:
                pos = index
                cur_sum = 0
        print(f"Max sub array between: {start} - {end}")
        return max_sum


if __name__ == "__main__":
    subArrayObj = MaxSumSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    sum = subArrayObj.findMaxSumInSubArray()
    print(f"Sum : {sum}")

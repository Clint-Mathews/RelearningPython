import sys


class Chocolate:
    def __init__(self, items, m):
        self.items = items
        self.m = m

    def findMinDifference(self):
        self.items.sort()
        i=0
        j = self.m-1
        min = sys.maxsize
        while j < len(self.items):
            diff = self.items[j] - self.items[i]
            if min > diff:
                min = diff
            i+=1
            j+=1

        return min


if __name__=="__main__":
    obj = Chocolate([3, 4, 1, 9, 56, 7, 9, 12], 5)
    print(f"diff:{obj.findMinDifference()}")

    obj2 = Chocolate([12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50], 7)
    print(f"diff:{obj2.findMinDifference()}")

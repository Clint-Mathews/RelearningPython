class Solution:
    def insert(self, intervals, newInterval):
        for i in intervals:
            if (newInterval[0] >= i[0] and newInterval[0] <= i[1]) or (newInterval[1] >= i[0] and newInterval[1] <= i[1]):
                index = intervals.index(i)
                minValue = 0
                maxValue = 0
                if newInterval[0] > i[0]:
                    minValue = i[0]
                else:
                    minValue = newInterval[0]

                if newInterval[1] > i[1]:
                    maxValue = newInterval[1]
                else:
                    maxValue = i[1]
                newInterval= [minValue, maxValue]
                intervals.insert(index+1, newInterval)
                intervals.pop(index)
        for i in intervals:
            print(i)

d = Solution()
d.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])
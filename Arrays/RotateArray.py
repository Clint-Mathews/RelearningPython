

class Solution:
    def swap(self, nums, index1, index2):
        temp = nums[index1]
        nums[index1] = nums[index2]
        nums[index2] = temp

    def Bruterotate(self, nums, k) -> None:
        for i in range(k):
            for index,value in reversed(list(enumerate(nums))):
                if index > 0:
                    self.swap(nums, index, index-1)
        for index,value in enumerate(nums):
            print(index, value)
    def rotate(self, nums, k: int) -> None:
            k = k % len(nums)
            mid = len(nums) - 1 - k
            i = 0
            while (i < mid):
                self.swap(nums, i, mid)
                i += 1
                mid -= 1

            i = len(nums) - k
            end = len(nums) - 1
            while (i < end):
                self.swap(nums, i, end)
                i += 1
                end -= 1

            i = 0
            end = len(nums) - 1
            while (i < end):
                self.swap(nums, i, end)
                i += 1
                end -= 1
            for index,value in enumerate(nums):
                print(index, value)
d = Solution()
d.rotate([1,2,3,4,5,6,7],3)
d.Bruterotate([1,2,3,4,5,6,7],3)
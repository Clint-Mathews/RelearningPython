from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, data in enumerate(nums):
            print(index, data)
            check_val = target - data
            if str(check_val) in hash_map:
                return [index, hash_map[str(check_val)]]
            else:
                hash_map[str(data)] = index
        return []

if __name__ == '__main__':
    sol = Solution()
    data = [2, 7, 11, 15]
    target = 9
    res = sol.twoSum(data, target)
    print('Res: {}'.format(res))

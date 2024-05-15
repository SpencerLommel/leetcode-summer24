from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            newArray = nums.copy()
            newArray.remove(i)
            for n in newArray:
                if i + n == target:
                    return [nums.index(i), newArray.index(n) + 1]
        

nums = [3, 2, 4]
target = 6


sol = Solution()
print(sol.twoSum(nums=nums, target=target))
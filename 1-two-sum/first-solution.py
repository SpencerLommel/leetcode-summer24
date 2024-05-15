from typing import List

# This solution involves iterating over the list once and then copying the array without the first value and iterating over it again.
# Here are my submission stats
# Runtime 2232ms Beats 9.32% of users with Python3
# Memory 17.37MB Beats 84.36% of users with Python3

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
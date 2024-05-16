from typing import List

# This updated version involves iterating using the index positions as opposed to the values itself 
# using the index positions we can prevent removing, copying, and indexing which are all O(n) which makes this more efficient
# Here are my submission stats
# Runtime 1651ms Beats 32.98% of users with Python3
# Memory 17.38MB Beats 84.36% of users with Python3

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]





nums = [3, 3, 4]
target = 6


sol = Solution()
print(sol.twoSum(nums=nums, target=target))
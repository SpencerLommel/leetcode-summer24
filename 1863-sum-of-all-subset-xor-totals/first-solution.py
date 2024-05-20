# May 19th 2024 LC Daily Challenge
# This is very very inefficient but it works!
# Submission stats
# Runtime 115ms Beats 5.61% of users with Python3
# Memory 17.02 MB Beats 17.17% of users with Python3

from itertools import chain, combinations
from typing import List


class Solution:
    
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        subsets = (list(chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))))
        for s in subsets[1::]:
            print(list(s))
            local_total = None
            for i in list(s):
                if not local_total:
                    local_total = i
                else:
                    local_total = local_total ^ i
            total += local_total
        return total
        
    

nums = [5, 1, 6]
sol = Solution()

print(sol.subsetXORSum(nums=nums))


# total = None
# for i in nums:
#     if not total:
#         total = i
#     else:
#         total = total ^ i
# print(total)
    
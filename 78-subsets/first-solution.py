# May 19th 2024 LC Daily Challenge
# Uses chain and combinations to get all subsets efficiently 
# Submission stats
# Runtime 34ms Beats 77.09% of users with Python3
# Memory 16.71 MB Beats 30.01% of users with Python3


from itertools import chain, combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        subsets = (list(chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))))
        for s in subsets:
            all_subsets.append(list(s))
        return all_subsets


nums = [1, 2, 3]
sol = Solution()
print(sol.subsets(nums=nums))
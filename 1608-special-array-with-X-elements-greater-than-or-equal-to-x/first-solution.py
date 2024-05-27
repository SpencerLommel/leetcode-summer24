# This problem can be improved by sorting the array first and then using a single pass to determine the special value
# Runtime 45ms Beats 34.01% of users with Python3
# Memory 16.40MB Beats 86.58% of users with Python3

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            counter = 0
            for k in nums:
                if k > i:
                    counter += 1
            if counter == i + 1:
                return i + 1
        else:
            return -1

        

sol = Solution()

nums = [0,4,3,0,4]
print(sol.specialArray(nums=nums))
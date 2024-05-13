# This is a very simple solution but not time efficient as it has to convert the entire list into a set and then back into a list.
# Here are my submission stats 446ms Beats 24.23% of users with Python

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not (len(nums) <= len(list(set(nums))))
        

sol = Solution()

nums = [1,2,3,4]
print(sol.containsDuplicate(nums=nums))

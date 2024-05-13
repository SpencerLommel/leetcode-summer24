# This solution was more complicated with iterating over the list and then if the value was seen returning True and if not adding it to a set of seen values
# My submission stats were 427ms Beats 64.75% of users with Python

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seenValues = set() # I first tried this with a list but it was very slow and exceeded the time limit on LC. After switching to a set() it was much faster
        for n in nums:
            if n in seenValues:
                return True
            seenValues.add(n)
        return False
        

sol = Solution()

nums = [1,2,3,4]
print(sol.containsDuplicate(nums=nums))
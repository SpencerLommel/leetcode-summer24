# This solution involves creating a new empty string and iterating over each char in the original string and appending all alphanumeric values to the new string
# Then comparing them forwards and backwards to see if they are equal
# Here are my submission stats
# Runtime 36 Beats 93.41% of users with Python3
# Memory 17.04MB Beats 63.24% of users with Python3

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        s = s.lower()
        for c in s:
            if c.isalnum():
                new_string += c

        return new_string == new_string[::-1]
        


s = "A man, a plan, a canal: Panama"

sol = Solution()
print(sol.isPalindrome(s=s))
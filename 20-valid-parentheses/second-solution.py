# This solution prevents creating the dict for a precheck and just returning False if there is still contents in the stack
#Submission stats
# Runtime 34ms Beats 67.30% of users with Python3
# Memory 16.61MB Beats 22.70% of users with Python3

from typing import Counter


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False 
                else:
                    if stack.pop(-1) != closing[c]:
                        return False
        
        return len(stack) == 0

                
    
        
            
s = "(){}}{"

sol = Solution()
print(sol.isValid(s=s))
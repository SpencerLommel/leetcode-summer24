# This feels like a pretty bad solution and I'll have to come back eventually and find a better solution
#Submission stats
# Runtime 37ms Beats 46.50% of users with Python3
# Memory 16.64MB Beats 22.70% of users with Python3

from typing import Counter


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        dictCounter = Counter(s)
        if dictCounter["["] != dictCounter["]"] or dictCounter["("] != dictCounter[")"] or dictCounter["{"] != dictCounter["}"]:
            return False

        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False 
                elif c == ")":
                    if stack.pop(-1) != "(":
                        return False
                elif c == "}":
                    if stack.pop(-1) != "{":
                        return False
                elif c == "]":
                    if stack.pop(-1) != "[":
                        return False
        return True

                
    
        
            
s = "(){}}{"

sol = Solution()
print(sol.isValid(s=s))
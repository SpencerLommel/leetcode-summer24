from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        pass
        

s = "aab"
sol = Solution()
print(sol.partition(s=s))



s1 = ["a", "b"]
s2 = ["b", "a"]

print(s1[::-1] == s2)

palindromes = []
stack = [s[0]]
print(stack)
for c in range(1, len(s)):
    stack.append(s[c])
    
    if stack[::-1] != stack:
        stack.pop(-1)
        palindromes.append(stack)

print(palindromes)
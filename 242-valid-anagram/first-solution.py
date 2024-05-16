# Converts both strings to dict with key being char and value being occurences and then compares if they're equal
# Submission stats
# Runtime 38ms Beats 94.83% of users with Python3
# Memory 17.08MB Beats 33.78% of users with Python3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sDict = { v:s.count(v) for v in set(s)}
        tDict = { v:t.count(v) for v in set(t)}

        return sDict == tDict

        


s = "rat"
t = "car"

sol = Solution()
print(sol.isAnagram(s=s, t=t))
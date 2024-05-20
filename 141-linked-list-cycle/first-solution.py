# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        


pos = 0
head = ListNode(1, ListNode(2))

sol = Solution()
print(sol.hasCycle(head=head, pos=pos))
# Definition for singly-linked list.
# Submission Stats
# Runtime 40ms Beats 45.33% of users with Python3
# Memory 16.45MB Beats 95.64% of users with Python3

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        tail = dummyNode

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummyNode.next
                


    def get_values(self, head: Optional[ListNode]) -> list:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

sol = Solution()

mergeSortedList = sol.mergeTwoLists(list1, list2)
print(sol.get_values(mergeSortedList))

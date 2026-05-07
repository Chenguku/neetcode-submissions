# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dict = {}
        while head:
            if head in dict.keys():
                return True
            dict[head] = True
            head = head.next
        return False
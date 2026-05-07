# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = False
        dummy = ListNode()
        sum = dummy
        while l1 or l2:
            if not l1:
                digit = l2.val
            elif not l2:
                digit = l1.val
            else:
                digit = l1.val + l2.val
            if flag:
                digit += 1
            if(digit > 9):
                flag = True
                digit -= 10
            else:
                flag = False
            sum.next = ListNode(digit, None)
            sum = sum.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if flag:
            sum.next = ListNode(1, None)
        return dummy.next
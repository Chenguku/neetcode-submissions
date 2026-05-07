# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# reverse from ptr to kptr
# 

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        kptr = dummy
        while True:
            for i in range(k):
                print(kptr.val)
                kptr = kptr.next
                if not kptr:
                    return dummy.next
            curr, prev, groupNext = groupPrev.next, kptr.next, kptr.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp2 = groupPrev.next
            groupPrev.next = kptr
            groupPrev = temp2
            kptr = groupPrev

        return dummy.next

            
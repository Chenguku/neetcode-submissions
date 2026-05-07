# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n*k) means go through every unmerged list once for every index

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        ptr = dummy
        while lists:
            lowest = float('inf')
            rm = 0
            for i in range(len(lists)):
                if not lists[i]: 
                    continue
                if lists[i].val < lowest:
                    lowest = lists[i].val
                    rm = i
            if lowest == float('inf'):
                break
            ptr.next = lists[rm]
            lists[rm] = lists[rm].next
            ptr = ptr.next

        return dummy.next


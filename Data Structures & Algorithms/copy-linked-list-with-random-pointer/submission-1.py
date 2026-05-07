"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        newHead = Node(head.val, head.next, head.random)
        cur = head.next
        nodeDict = {}
        nodeDict[head] = newHead
        while cur:
            newNode = Node(cur.val, cur.next, cur.random)
            nodeDict[cur] = newNode
            cur = cur.next

        ptr = newHead
        while ptr:
            ptr.next = nodeDict.get(ptr.next)
            ptr.random = nodeDict.get(ptr.random)
            ptr = ptr.next
        return newHead
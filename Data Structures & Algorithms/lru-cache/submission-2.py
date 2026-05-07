class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = self

class LRUCache:

    def __init__(self, capacity: int):
        self.maxSize = capacity
        self.size = 0
        self.map = {}
        self.dummy = Node(0, 0)

    def get(self, key: int) -> int:
        if key in self.map.keys():
            Node = self.map[key]
            Node.prev.next = Node.next
            Node.next.prev = Node.prev
            Node.next = self.dummy.next
            Node.prev = self.dummy
            self.dummy.next.prev = Node
            self.dummy.next = Node
            return Node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map.keys():
            rm = self.map[key]
            rm.next.prev = rm.prev
            rm.prev.next = rm.next
            del self.map[key]
            self.size -= 1
        newNode = Node(key, value)
        newNode.next = self.dummy.next
        newNode.prev = self.dummy
        self.dummy.next.prev = newNode
        self.dummy.next = newNode
        self.map[key] = newNode
        self.size += 1

        if self.size <= self.maxSize:
            return
        del self.map[self.dummy.prev.key]
        self.dummy.prev.prev.next = self.dummy
        self.dummy.prev = self.dummy.prev.prev
        self.size -= 1

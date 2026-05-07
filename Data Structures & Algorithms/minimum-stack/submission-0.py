class MinStack:
    def __init__(self):
        self.stack = []
        self.prefixMins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.prefixMins) != 0:
            self.prefixMins.append(min(val, self.prefixMins[-1]))
        else:
            self.prefixMins.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.prefixMins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefixMins[-1]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a) + int(b))
            elif i == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) - int(a))
            elif i == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a) * int(b))
            elif i == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) / int(a))
            else:
                stack.append(i)
        return int(stack[0])
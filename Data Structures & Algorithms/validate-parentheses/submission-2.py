class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')' and (len(stack) == 0 or stack.pop() != '('):
                return False
            elif i == ']' and (len(stack) == 0 or stack.pop() != '['):
                return False
            elif i == '}' and (len(stack) == 0 or stack.pop() != '{'):
                return False
        return len(stack) == 0
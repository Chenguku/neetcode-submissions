class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, j in enumerate(temperatures):
            while stack and j > stack[-1][0]: #index of last number
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex
            stack.append((j, i))
        return result
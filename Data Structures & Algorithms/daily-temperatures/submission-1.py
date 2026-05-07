class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[len(stack) - 1][1]:
                index = stack.pop()[0]
                results[index] = i - index
            stack.append((i, temperatures[i]))
        return results
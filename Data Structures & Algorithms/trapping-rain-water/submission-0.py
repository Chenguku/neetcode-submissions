# each index we either 
# add current water or 

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 0
        prefix = [0]
        suffix = [0]
        for i in range(len(height) - 1):
            prefix.append(max(height[i], prefix[len(prefix) - 1])) 
            suffix.append(max(height[len(height) - i - 1], suffix[len(suffix) - 1]))
        suffix.reverse()
        print(prefix)
        print(suffix)

        area = 0
        for i in range(len(height)):
            area += max(min(prefix[i], suffix[i]) - height[i], 0)
        return area

        
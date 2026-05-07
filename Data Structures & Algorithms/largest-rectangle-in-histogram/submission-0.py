class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        maxArea = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                area = heights[stack.pop()] * (i - stack[-1] - 1)
                if area > maxArea:
                    maxArea = area
            stack.append(i)
            if(heights[i]) > maxArea:
                maxArea = heights[i]

        while stack[-1] != -1:
            area = heights[stack.pop()] * (len(heights) - stack[-1] - 1)
            if area > maxArea:
                maxArea = area
        return maxArea

        # [2, 1] 5
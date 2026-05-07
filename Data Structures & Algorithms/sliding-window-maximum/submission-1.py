class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []
        mono = deque()
        l, r = 0, 0

        while r < len(nums):
            while mono and nums[mono[-1]] < nums[r]:
                mono.pop()
            mono.append(r)

            if l > mono[0]:
                mono.popleft()
            if (r + 1) >= k:
                maxes.append(nums[mono[0]])
                l += 1
            r += 1
        return maxes
            
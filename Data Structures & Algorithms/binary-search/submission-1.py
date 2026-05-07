class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while r >= l:
            if nums[(r + l) // 2] < target:
                l = (r + l) // 2 + 1
            elif nums[(r + l) // 2] > target:
                r = (r + l) // 2 - 1
            else:
                return (r + l) // 2
        return -1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # num:index
        for i in range(len(nums)):
            for j in seen:
                if nums[i] + j == target:
                    return [seen[j], i]
            seen[nums[i]] = i
        
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numSet = set()
        for i in range(len(nums)):
            if nums[i] in numSet: return nums[i]
            numSet.add(nums[i])
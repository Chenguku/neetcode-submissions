class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 1, 0;
        flag = 0
        while nums[fast] != nums[slow]:
            fast = (fast + 2) % len(nums)
            slow = (slow + 1) % len(nums)
            if fast == slow:
                fast = (fast + 1) % len(nums)
        return nums[fast]

# sorted array rotated at least once
# return the minimum element
# elements not necessarily 1 - n


class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
                break
            m = (l + r) // 2
            minimum = min(minimum, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return minimum
            
            

# [6, 1, 2, 3, 4, 5]
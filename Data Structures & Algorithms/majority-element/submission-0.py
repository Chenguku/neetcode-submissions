class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return [num for num, freq in count.most_common(1)][0]
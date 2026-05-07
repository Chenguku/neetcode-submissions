class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sequence = {}
        longest = 0
        for r in range(len(s)):
            if s[r] in sequence:
                l = max(l, sequence[s[r]] + 1)
            sequence[s[r]] = r
            if r - l + 1 > longest:
                longest = r - l + 1
            print(sequence)
        return longest
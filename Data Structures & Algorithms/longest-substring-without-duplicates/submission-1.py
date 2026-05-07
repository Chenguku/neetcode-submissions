class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sequence = set()
        longest = 0
        for r in range(len(s)):
            while s[r] in sequence:
                sequence.remove(s[l])
                l += 1
            sequence.add(s[r])
            if r - l + 1 > longest:
                longest = r - l + 1
        return longest
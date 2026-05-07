# Uppercase characters and int k
# k characters can be replace by another uppercase character
# after up to k replacements, what is the longest substring of one character
# O(n) time means i should probably only pass through once (can't be per letter thats O(n * m))
# O(m) space means im allowed to keep a value for each letter
# Hashmap is probably used to track characters within the window

# Want our window to track counts of letters 
# This way we can find greatest count of letters in range k
# So we can replace all other (x) letters and replace another k-x letters

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        windowLetters = {}
        greatestCount = 0
        for r in range(len(s)):
            windowLetters[s[r]] = windowLetters.get(s[r], 0) + 1
            while r - l >= k + max(windowLetters.values()) and l < len(s) - 1:
                windowLetters[s[l]] -= 1
                l += 1
            if max(windowLetters.values()) + k > greatestCount:
                greatestCount = max(windowLetters.values()) + k
        return min(greatestCount, len(s))
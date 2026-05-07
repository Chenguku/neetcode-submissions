class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict = {}
        window = {}
        for i in t:
            tDict[i] = tDict.get(i, 0) + 1
        
        l = 0
        have, need = 0, len(tDict)
        minLength = float('inf')
        minL, minR = 0, 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in tDict and window[s[r]] == tDict[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < minLength:
                    minLength = r - l + 1
                    minL, minR = l, r
                window[s[l]] -= 1
                if s[l] in tDict and window[s[l]] < tDict[s[l]]:
                    have -= 1
                l += 1
        return "" if minLength == float('inf') else s[minL: minR + 1]
# only contain lowercase letters
# can keep track of permutations via lettercounts
# don't want to check everything in the map every time (actually not a problem)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1letters = {}
        for i in s1:
            s1letters[i] = s1letters.get(i, 0) + 1

        l = 0
        s2window = {}
        for r in range(len(s2)):
            s2window[s2[r]] = s2window.get(s2[r], 0) + 1
            if r - l >= len(s1):
                s2window[s2[l]] -= 1
                if s2window[s2[l]] < 1:
                    del s2window[s2[l]]
                l += 1
            if r - l + 1 >= len(s1) and s2window == s1letters:
                return True

        return False
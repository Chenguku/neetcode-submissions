class Solution:
    def eatingTime(self, piles, k):
        time = 0
        for i in piles: 
            time += math.ceil(i / k)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = 0
        for i in piles:
            if i > maxPile:
                maxPile = i
        
        l, r = 1, maxPile
        result = maxPile
        while l <= r:
            m = (l + r) // 2
            if self.eatingTime(piles, m) <= h:
                result = m
                r = m - 1
            else:
                l = m + 1
        return result
        

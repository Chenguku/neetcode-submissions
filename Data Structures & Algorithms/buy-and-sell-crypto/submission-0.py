class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max = 0
        while r < len(prices):
            if prices[r] - prices[l] > max:
                max = prices[r] - prices[l]
            if prices[r] > prices[l] or l >= r:
                r += 1
            else:
                l += 1
        return max
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                result += prices[i] - prices[i-1]
        return result

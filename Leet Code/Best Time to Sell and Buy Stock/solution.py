class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        sell = 0
        for i in range(1, len(prices)):
            if sell > prices[i]:
                profit += sell - buy
                buy = prices[i]   
                sell = 0
            if prices[i] <= buy:
                buy = prices[i]
            else:
                sell = prices[i]
        if sell != 0:
            profit += sell - buy
        return profit
                

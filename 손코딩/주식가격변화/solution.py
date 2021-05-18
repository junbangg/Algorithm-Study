prices = [2, 5, 1, 0, 6, 3]
# 0 <= len(prices) < maxint
import sys
def getMaxProfit(prices):
    # edge case
    if not prices:
        return 0
    minPrice = sys.maxint
    maxProfit = -1
    # O(n)
    for price in prices:
        minPrice = min(minPrice, price)
        maxProfit = max(price - minPrice, maxProfit)
    return maxProfit





print(getMaxProfit(prices))


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy = prices[i]
            else:
                diff = prices[i]-buy
                sell = max(sell,diff)
        return sell
            # diff = prices
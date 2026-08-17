class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        buy = prices[0]

        if not prices:
            return 0
        
        for sell in prices:
            if sell > buy:
                profit = sell - buy
                maxprofit = max(profit,maxprofit)
            else:
                buy = sell
        return maxprofit
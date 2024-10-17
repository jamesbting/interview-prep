class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = -math.inf
        sell = 0

        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)
    
        return sell
        
        
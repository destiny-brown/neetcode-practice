class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, prices[0]

        for today_price in prices:
            max_profit = max(max_profit, today_price - min_price)
            min_price = min(min_price, today_price)
        
        return max_profit
        
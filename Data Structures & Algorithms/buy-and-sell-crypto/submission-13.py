class Solution:
        def maxProfit(self, prices: List[int]) -> int:


            max_pro = 0
            min_prices = prices[0]

            for price in prices:
                max_pro = max(max_pro, price - min_prices)
                min_prices = min(min_prices, price)

            return max_pro




























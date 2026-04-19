class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        max_pro =  0

        min_prices = prices[0]


        for i in prices :

            max_pro = max (max_pro , i - min_prices)

            min_prices = min (min_prices , i)

        return max_pro    




















        





        






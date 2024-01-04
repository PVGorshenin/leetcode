class Solution:

    def maxProfit(self, prices, fee):

        min_price = prices[0]
        profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            elif price > min_price + fee:
                profit += price - (min_price + fee)
                min_price = price - fee

        return profit



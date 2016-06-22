import sys
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        buy = sys.maxint
        max_profit = 0
        for price in prices:
            if price < buy:
                buy = price
            if price - buy > max_profit:
                max_profit = price - buy
        return max_profit

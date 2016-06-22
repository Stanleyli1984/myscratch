class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        buy = 0
        last_idx = len(prices) - 1
        profit = 0
        for idx, price in enumerate(prices):
            if (idx == 0 or prices[idx - 1] >= prices[idx]) and (idx != last_idx and prices[idx+1] > prices[idx]):
                buy = price
            elif (idx != 0 and prices[idx - 1] < prices[idx]) and (idx == last_idx or prices[idx+1] <= prices[idx]):
                profit += price - buy
        return profit
class Solution:
    # @param prices, a list of integer
    # @return an integer
    buys = []
    sells = []

    def __init__(self):
        self.buys = []
        self.sells = []

    def maxProfit(self, prices):
        last_idx = len(prices) - 1
        max_profit = 0
        for idx, price in enumerate(prices):
            if (idx == 0 or prices[idx - 1] >= prices[idx]) and (idx != last_idx and prices[idx+1] > prices[idx]):
                self.buys.append(price)
            elif (idx != 0 and prices[idx - 1] < prices[idx]) and (idx == last_idx or prices[idx+1] <= prices[idx]):
                self.sells.append(price)

        for i in xrange(0, len(self.buys)):
            profit = self.calculate_profits(self.buys[0:i], self.sells[0:i]) + self.calculate_profits(self.buys[i:], self.sells[i:])
            if max_profit < profit:
                max_profit = profit
        return max_profit

    def calculate_profits(self, buys, sells):
        if not buys:
            return 0
        else:
            max_profit = 0
            for idx, buy in enumerate(buys):
                if max_profit < max(sells[idx:]) - buy:
                    max_profit = max(sells[idx:]) - buy
        return max_profit

Solution().maxProfit([1,2, 1,2])
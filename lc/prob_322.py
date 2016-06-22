class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [float('inf')] * amount
        for i in xrange(1, amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] + 1 < dp[i]:
                        dp[i] = dp[i - coin] + 1
                    #dp[i] = min(dp[i - coin] + 1, dp[i])
        if dp[-1] < float('inf'):
            return dp[-1]
        else:
            return -1

print Solution().coinChange([2], 10)
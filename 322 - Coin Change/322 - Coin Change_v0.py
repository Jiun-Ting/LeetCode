class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            Min = amount + 1
            for coin in coins:
                if i - coin >= 0 and dp[i-coin] > -1:
                     Min = min(Min, dp[i-coin])
            if Min < amount + 1:
                dp[i] = Min + 1
        return dp[amount]

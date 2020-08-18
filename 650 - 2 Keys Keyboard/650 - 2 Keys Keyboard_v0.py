class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        dp[0] = dp[1] = 0
        for i in range(2, n+1):
            for k in range(i/2, 1, -1):
                if i%k == 0:
                    dp[i] =  dp[k] + i/k
                    break

        return dp[n]

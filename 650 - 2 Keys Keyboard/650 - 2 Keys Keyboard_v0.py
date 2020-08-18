class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        for i in range(2, n+1):
            Min = i
            for k in range(2, i/2+1):
                if i%k == 0:
                    Min = min(Min, dp[k] + i/k)
            dp[i] = Min
        return dp[n]

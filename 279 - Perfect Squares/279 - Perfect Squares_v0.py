class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        N = [i**2 for i in range(1, int(sqrt(n))+1)]
        dp = [0]*(n+1)
        for i in range(1, n+1):
            Min = n
            for j in N:
                if i - j >= 0:
                    Min = min(dp[i-j], Min)
            dp[i] = Min + 1
        return dp[n]

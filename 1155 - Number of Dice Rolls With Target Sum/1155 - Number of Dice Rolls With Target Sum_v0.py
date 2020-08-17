class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        dp = [[0 for j in range(target+1)] for i in range(d+1)]
        for i in range(1, f+1):
            if i <= target:
                dp[1][i] = 1
        for i in range(1, d+1):
            for j in range(1, target+1):
                Sum = 0
                for num in range(1, f+1):
                    if j-num>=0:
                        Sum += dp[i-1][j-num]
                dp[i][j] += Sum%(10**9+7)
        return dp[d][target]

        

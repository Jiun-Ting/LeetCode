class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        Max = 0
        for i in range(m):
            for j in range(n):
               dp[i][j] = int(matrix[i][j])
               if dp[i][j]:
                    Max = 1
        for i in range(1, m):
            for j in range(1, n):
                if dp[i-1][j-1] >= 1 and dp[i-1][j] >= 1 and dp[i][j-1] >= 1 and dp[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1],  dp[i-1][j],  dp[i][j-1])+1
                    Max = max(Max, dp[i][j])
        return Max**2

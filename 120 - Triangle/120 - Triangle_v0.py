class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[0][i] = A[0][i]

        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i-1][j+1])
                elif j == n-1:
                    dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i-1][j-1])
                else:
                    dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i-1][j+1], dp[i-1][j-1])
        print(dp)
        return min(dp[n-1][i] for i in range(n))

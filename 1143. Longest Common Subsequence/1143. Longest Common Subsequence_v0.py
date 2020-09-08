class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        L1 = len(text1)
        L2 = len(text2)
        dp = [[0 for j in range(L2+1)] for i in range(L1+1)]
        for i in range(1, L1+1):
            for j in range(1, L2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] =  max(dp[i-1][j], dp[i][j-1])

        return dp[L1][L2]

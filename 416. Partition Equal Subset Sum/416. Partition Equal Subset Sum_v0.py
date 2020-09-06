class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        S = sum(nums)
        if S%2==1:
            return False
        S /= 2
        n = len(nums)

        dp = [[False for i in range(n+1)] for j in range(S+1)]
        for i in range(n+1):
            dp[0][i] = True
        for i in range(1, n+1):
            for j in range(1, S+1):
                if j-nums[i-1] >= 0:
                    dp[j][i] = (dp[j][i-1] or dp[j-nums[i-1]][i-1])
                else:
                    dp[j][i] =  dp[j][i-1]
        return dp[S][n]

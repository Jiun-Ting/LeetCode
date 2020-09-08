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

        dp = [False for i in range(S+1)]
        dp[0] = True
        for i in nums:
            for j in reversed(range(S+1)):
                if j >= i:
                    dp[j] = dp[j] or dp[j-i]
        return dp[S]

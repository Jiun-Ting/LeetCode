class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = collections.defaultdict(int)
        dp[0] = 1
        for i in nums:
            N = collections.defaultdict(int)
            for j in dp:
                N[j-i] += dp[j]
                N[j+i] += dp[j]
            dp = N

        return dp[S]

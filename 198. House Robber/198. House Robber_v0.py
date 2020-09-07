class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.append(0)
        dp = [0]*(n+3)
        for i in reversed(range(n)):
            dp[i] = max(nums[i]+dp[i+2], nums[i+1]+dp[i+3])
        return dp[0]

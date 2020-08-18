class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        n = days[-1]
        dp = [0]*(n+1)
        for i in range(days[0], n+1):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                if i-30 < 0:
                    dp[i] = min(dp[i-1]+costs[0], dp[i-7]+costs[1], costs[2])
                elif i-7 < 0:
                    dp[i] = min(dp[i-1]+costs[0], costs[1], costs[2])
                else:
                    dp[i] = min(dp[i-1]+costs[0], dp[i-7]+costs[1], dp[i-30]+costs[2])
        return dp[n]

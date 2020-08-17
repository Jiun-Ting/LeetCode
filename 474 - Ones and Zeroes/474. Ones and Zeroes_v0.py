class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        p = [(sum([1 for o in i if o=="0"]), sum([1 for z in i if z!="0"])) for i in strs]
        for k in p:
            for i in range(m,-1,-1):
                for j in range(n,-1,-1):
                    if i-k[0]>=0 and j-k[1] >= 0:
                        dp[i][j] = max(dp[i][j], dp[i-k[0]][j-k[1]]+1)

        return dp[m][n]

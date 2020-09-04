class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        r = [sum(grid[i]) for i in range(m)]
        c  =[0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                c[j] += grid[i][j]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (r[i] >= 2 or c[j] >= 2):
                    ans += 1
        return ans

           

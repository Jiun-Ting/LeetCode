class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def DFS(i, j):
            grid[i][j] = 1
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                    DFS(x, y)

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i == 0 or i==m-1 or j == 0 or j == n-1) and grid[i][j] == 0:
                    DFS(i, j)
        ans = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 0:
                    ans += 1
                    DFS(i, j)

        return ans

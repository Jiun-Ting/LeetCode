class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def BFS(i, j):
            q = collections.deque([(i, j)])
            while q:
                r, c = q.popleft()
                for x, y in [(r+1, c), (r-1,c), (r, c+1), (r, c-1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                        grid[x][y] = "0"
                        q.append((x, y))
        ans = 0
        if not grid or not grid[0]:
            return ans
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    BFS(i, j)

        return ans

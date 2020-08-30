class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def BFS(sr,sc):
            area = 1
            q = collections.deque([(i,j)])
            grid[i][j] = -1
            while q:
                vr, vc = q.popleft()
                for (x, y) in [(vr+1, vc), (vr-1, vc), (vr, vc+1), (vr, vc-1)]:
                    if  0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        q.append((x, y))
                        grid[x][y] = -1
                        area += 1
            return area


        m, n = len(grid), len(grid[0])
        Max = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    Max = max(Max, BFS(i, j))
        return Max

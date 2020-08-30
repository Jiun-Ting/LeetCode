class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        R = -1
        q = collections.deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))

        if len(q) != m*n:
            while q:
                count =  len(q)
                R += 1
                while count:
                    vr, vc = q.popleft()
                    count -= 1
                    for (x, y) in [(vr, vc+1), (vr, vc-1), (vr+1, vc), (vr-1, vc)]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                            q.append((x, y))
                            grid[x][y] = 1
        return R

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        q = collections.deque([])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if q:
            R = -1
        else:
            R = 0
        while q:
            count = len(q)
            while count > 0:
                vr, vc = q.popleft()
                count -= 1
                for (x, y) in [(vr+1, vc), (vr-1, vc), (vr, vc+1), (vr, vc-1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        q.append((x, y))
                        grid[x][y] = 2
                        fresh -= 1
            R += 1

        if fresh > 0: return -1
        return R

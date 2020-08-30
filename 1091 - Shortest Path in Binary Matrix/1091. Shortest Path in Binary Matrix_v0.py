class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1
        Finish = False
        m, n = len(grid), len(grid[0])
        q = collections.deque([(0,0)])
        grid[0][0] = 1
        D = 0
        while q:
            count = len(q)
            D += 1
            while count:
                r, c = q.popleft()
                if (r, c) == (m-1, n-1):
                    return D
                count -= 1
                for (x, y) in [(r, c+1), (r, c-1), (r+1, c), (r-1,c), (r+1, c+1), (r-1, c-1), (r+1, c-1), (r-1, c+1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                        q.append((x, y))
                        grid[x][y] = 1
        return -1

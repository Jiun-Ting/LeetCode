class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        def BFS(i, j):
            q = collections.deque([(i,j)])
            A[i][j] = 0
            while q:
                r, c = q.popleft()
                for (x, y) in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
                    if 0 <= x < m  and 0 <= y < n and A[x][y] == 1:
                        A[x][y] = 0
                        q.append((x, y))


        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and A[i][j]==1:
                    BFS(i, j)
        area = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                area += A[i][j]
        return area

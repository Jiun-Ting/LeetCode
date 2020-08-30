class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        R = 0
        ans = [[0 for j in range(n)] for i in range(m)]
        q = collections.deque([])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j))
        while q:
            count = len(q)
            R += 1
            while count:
                r, c = q.popleft()
                count -= 1
                for (x, y) in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] == 1:
                        q.append((x, y))
                        matrix[x][y] = 0
                        ans[x][y] = R
        return ans

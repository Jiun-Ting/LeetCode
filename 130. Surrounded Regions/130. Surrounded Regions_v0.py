class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def BFS(i, j):
            q = collections.deque([(i, j)])
            board[i][j] = "P"
            while q:
                r, c = q.popleft()
                for (x, y) in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
                    if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                        q.append((x, y))
                        board[x][y] = "P"
        if not board or not board[0]: return

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and board[i][j] =='O':
                    BFS(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "P":
                    board[i][j] = "O"

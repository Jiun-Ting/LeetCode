class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def DFS(i):
            for j in range(m):
                if  M[i][j] == 1:
                    M[j][j] = 0
                    M[i][j] = 0
                    M[j][i] = 0
                    DFS(j)
        m = len(M)
        ans = 0
        for i in range(m):
            if M[i][i] == 1:
                M[i][i] = 0
                ans += 1
                DFS(i)
        return ans

class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        def find(i):
            while i != parent[i]:
                i = parent[i]
            return i

        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return False
            parent[rootx] = rooty
            self.count += 1
            return True

        parent = [i for i in range(n)]
        self.count = 0
        r = 0
        for c in connections:
            if not union(c[0], c[1]):
                r += 1

        if r >= n - self.count-1:
            return n - self.count -1
        return -1

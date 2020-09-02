class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = [i for i in range(len(edges)+1)]
        def find(i):
            while i != parent[i]:
                i = parent[i]
            return i

        def Union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return False
            parent[rootx] = rooty
            return True

        for e in edges:
            if not Union(e[0], e[1]):
                return e

class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        parent = {c:c for c in string.lowercase}

        for e in equations:
            if e[1] == "=":
                parent[find(e[0])] = find(e[3])

        for e in equations:
            if e[1] == "!" and find(e[0]) == find(e[3]):
                return False
        return True

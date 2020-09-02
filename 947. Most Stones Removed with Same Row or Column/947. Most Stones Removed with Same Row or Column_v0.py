class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        def DFS(i):
            for s in r[stones[i][0]]+c[stones[i][1]]:
                if v[s] == 0:
                    v[s] = 1
                    self.ans += 1
                    DFS(s)

        n = len(stones)
        v = [False]*n
        r = collections.defaultdict(list)
        c = collections.defaultdict(list)
        for i, s in enumerate(stones):
            r[s[0]].append(i)
            c[s[1]].append(i)
        self.ans = 0
        for i in range(n):
            if v[i] == 0:
                v[i] = 1
                DFS(i)
        return self.ans

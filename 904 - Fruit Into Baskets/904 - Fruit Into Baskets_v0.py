class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        l = 0
        ans = 0
        C = collections.Counter()
        for r, v in enumerate(tree):
            C[v] += 1
            while l <= r and len(C) > 2:
                if C[tree[l]] == 1:
                    del C[tree[l]]
                else:
                    C[tree[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans

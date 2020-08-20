class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        ans = 0
        C = collections.Counter()
        for r, v in enumerate(s):
            C[v] += 1
            while l <= r and len(C)==3:
                ans += len(s) - r
                if C[s[l]] == 1:
                    del C[s[l]]
                else:
                    C[s[l]] -= 1
                l += 1
        return ans

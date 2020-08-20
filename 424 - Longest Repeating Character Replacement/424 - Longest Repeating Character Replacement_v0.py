class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        chars = set(s)
        ans = 0
        for char in chars:
            l = 0
            Sum = 0
            for r, v in enumerate(s):
                if v != char:
                    Sum += 1
                while l <= r and Sum > k:
                    if s[l] != char:
                        Sum -= 1
                    l += 1
                ans = max(ans, r-l+1)
        return ans

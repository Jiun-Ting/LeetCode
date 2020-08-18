class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        ans = 0
        for r, v in enumerate(s):
            while v in s[l:r]:
                l += 1
            ans = max(ans, r-l+1)
        return ans

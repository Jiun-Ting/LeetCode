class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        l = 0
        ans = 0
        D = [abs(ord(s[i])-ord(t[i])) for i in range(len(s))]
        for r, v in enumerate(D):
            maxCost -= v
            while l <= r and maxCost < 0:
                maxCost += D[l]
                l += 1
            ans = max(ans, r-l+1)
        return ans

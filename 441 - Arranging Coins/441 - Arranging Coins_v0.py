class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n+1
        while l < r:
            mid = (l+r)/2
            if (1+mid)*mid/2 > n:
                r = mid
            else:
                l = mid + 1
        return l-1

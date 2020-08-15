class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def condition(t):
            return sum((i - 1) // t + 1 for i in piles) <= H


        l, r = 1, max(piles)
        while l < r:
            mid = (l + r)//2
            if condition(mid):
                r = mid
            else:
                l = mid + 1
        return l

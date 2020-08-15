class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        def condition(c):
            total = 0
            Day = 1
            for w in weights:
                total += w
                if c < w:
                    return False
                if total > c:
                    total = w
                    Day += 1
                    if Day > D:
                        return False
            return Day <= D

        l, r = 1, sum(weights)
        while l < r:
            mid = (l + r)//2
            if condition(mid):
                r = mid
            else:
                l = mid + 1
        return l

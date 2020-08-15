class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

    def peakIndexInMountainArray(self, A):
        l, r = 0, len(A) - 1
        while l < r:
            m = (l + r) / 2
            if A[m] >= A[m + 1]:
                r = m
            else:
                l = m + 1
        return l
        

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def getMinMax(v):
            total = 0
            count = 1
            for i in nums:
                total += i
                if total > v:
                    count += 1
                    total = i
            return count <= m

        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r)//2
            if getMinMax(mid):
                r = mid
            else:
                l = mid +1
        return l

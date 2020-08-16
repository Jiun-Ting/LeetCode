class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def condition(d):
            return sum((i-1)/d+1 for i in nums) <= threshold

        l, r = 1, max(nums)
        while l < r:
            mid = (l + r)//2
            if condition(mid):
                r = mid
            else:
                l = mid + 1
        return l

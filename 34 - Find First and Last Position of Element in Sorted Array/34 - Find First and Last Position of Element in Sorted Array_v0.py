class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return [-1, -1]
        def bs(t):
            l, r = 0, n
            while l < r:
                mid = (l+r)//2
                if nums[mid] >= t:
                    r = mid
                else:
                    l = mid + 1
            return l
        if bs(target) == n or nums[bs(target)] != target:
            return [-1, -1]
        return [bs(target), bs(target+1)-1]

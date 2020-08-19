class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        P = 1
        ans = 0
        for r, v in enumerate(nums):
            P *= v
            while l <= r and P >= k:
                P /= nums[l]
                l += 1
            ans += r - l + 1
        return ans

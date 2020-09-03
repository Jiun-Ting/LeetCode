class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(nums)
        l, r = 0, len(nums)-1
        while l < r and nums[r] == s[r]: r -= 1
        while l <= r and  nums[l] == s[l]: l += 1


        return r-l+1

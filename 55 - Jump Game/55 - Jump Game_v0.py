class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = 0
        for i in range(len(nums)-1):
            if last >= i:
                last = max(last, i + nums[i])
        return last >= len(nums)-1

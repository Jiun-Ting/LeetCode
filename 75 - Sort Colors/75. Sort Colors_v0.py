class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = collections.defaultdict(int)
        for i in nums:
            count[i] += 1
        for i in range(count[0]):
            nums[i] = 0
        for i in range(count[0], count[0]+count[1]):
            nums[i] = 1
        for i in range(count[0]+count[1], len(nums)):
            nums[i] = 2
        return nums

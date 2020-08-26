class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==0:
            return
        curr = 1
        value = nums[0]
        i = 1
        while i < len(nums):
            while i < len(nums) and value >= nums[i]:
                i += 1
            if i < len(nums):
                nums[i], nums[curr] = nums[curr], nums[i]
                value = nums[curr]
                curr += 1

        return curr

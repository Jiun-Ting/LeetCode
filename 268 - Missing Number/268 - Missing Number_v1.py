class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, n = 0, len(nums)
        while i < n:
            j = nums[i]
            if j != i and j < n:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i, v in enumerate(nums):
            if i != v:
                return i
        return n
